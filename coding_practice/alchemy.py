from datetime import datetime, timezone

from sqlalchemy import CheckConstraint, Column, ForeignKey, String, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

# ==========================================
# MANY-TO-MANY ASSOCIATION TABLE
# ==========================================
# This table links Orders and MenuItems together behind the scenes
order_menu_item = Table(
    "order_menu_item",
    Base.metadata,
    Column("order_id", ForeignKey("orders.id", ondelete="CASCADE"), primary_key=True),
    Column("menu_item_id", ForeignKey("menuitems.id", ondelete="CASCADE"), primary_key=True),
)

# ==========================================
# MODELS
# ==========================================

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))
    last_login: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc), 
        onupdate=lambda: datetime.now(timezone.utc)
    )
    
    # 1. ONE-TO-ONE: One user has exactly one profile
    profile: Mapped["Profile"] = relationship(back_populates="user", cascade="all, delete-orphan")
    
    # 2. ONE-TO-MANY: One user can have a list of multiple orders
    orders: Mapped[list["Order"]] = relationship(back_populates="user", cascade="all, delete-orphan")


class Profile(Base):
    __tablename__ = "profiles"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    bio: Mapped[str | None] = mapped_column(String(500))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)

    user: Mapped["User"] = relationship(back_populates="profile")   


class Order(Base):
    __tablename__ = "orders"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    transaction_id: Mapped[str | None]
    
    user: Mapped["User"] = relationship(back_populates="orders")
    
    # 3. MANY-TO-MANY: An order has many menu items, using the secondary association table
    items: Mapped[list["MenuItems"]] = relationship(
        secondary=order_menu_item, 
        back_populates="orders"
    )


class MenuItems(Base):
    __tablename__ = "menuitems"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    is_available: Mapped[bool] = mapped_column(default=True)
    quantity: Mapped[int] = mapped_column(default=0)
    
    # Many-to-Many link back to orders
    orders: Mapped[list["Order"]] = relationship(
        secondary=order_menu_item, 
        back_populates="items"
    )
    
    # Fixed tuple comma so it parses as a valid tuple containing a constraint
    __table_args__ = (
        CheckConstraint("quantity >= 0", name="check_non_negative"),
    )
