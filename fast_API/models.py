from datetime import datetime, timezone
from decimal import Decimal

from enumeration import DeliveryStatus, OrderStatus, PaymentMethod, PaymentStatus
from sqlalchemy import CheckConstraint, ForeignKey, Numeric
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


# Restaurant → Customer → MenuItem → Order → OrderItem → Payment → Delivery
class Base(DeclarativeBase):
    ...


class Restaurant(Base):
    
    __tablename__ = "restaurant"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    address: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc)) # server_default = func.now()
    
    menu_items: Mapped[list["MenuItem"]] = relationship(back_populates="restaurant")


class Customer(Base):
    
    __tablename__ = "customers"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True) # regex implementation
    is_active: Mapped[bool] = mapped_column(default=True) # why is default always true??
    last_login: Mapped[datetime | None] = mapped_column(default=None) # how do I get the last login?? Will the logic get implemented when I am building the login endpoint?
    is_admin: Mapped[bool] = mapped_column(default=False)
    
    orders: Mapped[list["Order"]] = relationship(back_populates="customer")


class MenuItem(Base):
    
    __tablename__ = "menu_items" # (MenuItem = menuitem = MENUITEM) in the DB in an unqouted query
    
    id: Mapped[int] = mapped_column(primary_key=True)
    restaurant_id: Mapped[int] = mapped_column(ForeignKey("restaurant.id"))
    
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str | None]

    price: Mapped[Decimal] = mapped_column(Numeric(10, 2)) # max_digits before decimal is '10 - 2' then round up decimal points to 2.
    is_available: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))
    
    restaurant: Mapped["Restaurant"] = relationship(back_populates="menu_items")
    order_items: Mapped[list["OrderItem"]] = relationship(back_populates="menu_item")


class Order(Base):
    
    __tablename__ = "orders"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    
    status: Mapped[OrderStatus] = mapped_column(SQLEnum(OrderStatus), default=OrderStatus.PENDING) # SideNote = Line 1 in notes.txt
    total_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=0)
    
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc)) # Note: on_update works with session.commit
    
    customer: Mapped["Customer"] = relationship(back_populates="orders")
    items: Mapped[list["OrderItem"]] = relationship(back_populates="order", cascade="all, delete-orphan")
    
    payment: Mapped["Payment | None"] = relationship(back_populates="order", uselist=False)
    delivery: Mapped["Delivery | None"] = relationship(back_populates="order", uselist=False)


class OrderItem(Base):
    
    __tablename__ = "order_items"
    
    id: Mapped[int] = mapped_column(primary_key=True)

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), ondelete="CASCADE")
    menu_item_id: Mapped[int] = mapped_column(ForeignKey("menu_items.id"))

    quantity: Mapped[int]
    unit_price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    
    order: Mapped["Order"] = relationship(back_populates="items")
    menu_item: Mapped["MenuItem"] = relationship(back_populates="order_items")
    
    __table_args__ = (
        CheckConstraint("quantity >= 1", name="check_quantity_positive"),
        CheckConstraint("unit_price >= 0", name="check_unit_price_non_negative"),
    )
    

class Payment(Base):
    
    __tablename__ = "payments"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), unique=True)
    
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    method: Mapped[PaymentMethod] = mapped_column(SQLEnum(PaymentMethod), default=PaymentMethod.CASH)
    status: Mapped[PaymentStatus] = mapped_column(SQLEnum(PaymentStatus), default=PaymentStatus.AWAITING)
    transaction_reference: Mapped[str | None] = mapped_column(unique=True)
    
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))
    
    order: Mapped["Order"] = relationship(back_populates="payment")   
    
    __table_args__ = (
        CheckConstraint("amount >= 0", name="check_payment_amount_non_negative"),
    )


class Delivery(Base):
    __tablename__ = "deliveries"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), unique=True)

    address: Mapped[str] = mapped_column()
    status: Mapped[DeliveryStatus] = mapped_column(SQLEnum(DeliveryStatus), default=DeliveryStatus.PENDING)
    
    delivery_fee: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=Decimal("0.00"))
    estimated_delivery_at: Mapped[datetime | None] = mapped_column(default=None)
    delivered_at: Mapped[datetime | None] = mapped_column(default=None) # trigger on status == deliverystatus.delivered

    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))
    order: Mapped["Order"] = relationship(back_populates="delivery")
    
    __table_args__ = (
        CheckConstraint("delivery_fee >= 0", name="check_delivery_fee_non_negative"),
    )
