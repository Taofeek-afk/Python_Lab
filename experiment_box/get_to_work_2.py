from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)


class Base(DeclarativeBase):
    pass


class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str]

    manager_id: Mapped[int | None] = mapped_column(
        ForeignKey("employees.id")
    )

    manager: Mapped[int | None] = relationship(
        "Employee",
        remote_side=[id],
        back_populates="employees",
    )

    employees: Mapped[list[Employee]] = relationship(
        "Employee",
        back_populates="manager",
    )

    def __repr__(self) -> str:
        return (
            f"Employee(id={self.id}, "
            f"name={self.name!r}, "
            f"manager_id={self.manager_id})"
        )
