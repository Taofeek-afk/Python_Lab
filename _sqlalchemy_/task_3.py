from decimal import Decimal
from enum import StrEnum

from sqlalchemy import Column, Enum, ForeignKey, Numeric, Table
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship

Base = declarative_base()

# one-to-many

class Author(Base):
    
    __tablename__ = "authors"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    books: Mapped[list["Book"]] = relationship(back_populates="author")
    

class Book(Base):
    
    __tablename__ = "books"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    genre: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    
    author: Mapped["Author"] = relationship(back_populates="books")



# one-to-one

class Artist(Base):
    __tablename__ = "artists"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    genre: Mapped[str]
    
    biography: Mapped["Biography"] = relationship(back_populates="artist")
    

class Biography(Base):
    
    __tablename__ = "biography"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    body: Mapped[str]
    artist_id: Mapped[int] = mapped_column(ForeignKey("artists.id"), unique=True)
    artist: Mapped["Artist"] = relationship(back_populates="biography")



# many-to-many: Table

student_courses = Table(
    "student_courses",
    Base.metadata,
    Column("student_id", ForeignKey("students.id"), primary_key=True),
    Column("course_id", ForeignKey("courses.id"), primary_key=True),
)


class Student(Base):
    __tablename__ = "students"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    courses: Mapped[list["Course"]] = relationship(secondary="student_courses", back_populates="students")


class Course(Base):
    __tablename__ = "courses"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    
    students: Mapped[list["Student"]] = relationship(secondary="student_courses", back_populates="courses")


# many-to-many: model
class MenuOrder(Base):
    __tablename__ = "menu_orders"
    
    menu_id: Mapped[int] = mapped_column(ForeignKey("menus.id"), primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), primary_key=True)
    quantity: Mapped[int]
    
    menu: Mapped["Menu"] = relationship(back_populates="menu_orders")
    order: Mapped["Order"] = relationship(back_populates="menu_orders") 
    


class Menu(Base):
    __tablename__ = "menus"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))

    menu_orders: Mapped[list["MenuOrder"]] = relationship(back_populates="menu")
    
    

class Order(Base):
    __tablename__ = "orders"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    menu_orders: Mapped[list["MenuOrder"]] = relationship(back_populates="order")
    user: Mapped["User"] = relationship(back_populates="orders")


class UserRole(StrEnum):
    CUSTOMER = "customer"
    ADMIN = "admin"
    STAFF = "staff"


class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.CUSTOMER)
    
    orders: Mapped[list["Order"]] = relationship(back_populates="user")


#  user = User(name="Taofeek", role="admin")
#  Let's sat users have made orders and they are linked how do I access it?
# user.orders[0].menu_orders[0].name?


# from sqlalchemy import func

# count_stmt = select(
#     func.count(MenuItem.id)
# )

# total = await session.scalar(count_stmt)
# total_pages = math.ceil(total / limit)


# Find all menu items costing more than ₦5,000.

# Which one?

# A. WHERE
# B. HAVING
# C. EXISTS
# D. GROUP BY

# stmt = select(Restaurant).join(Restaurant.menuItems).where(MenuItems.price) > 5,000