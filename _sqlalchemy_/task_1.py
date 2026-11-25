from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship

Base = declarative_base()

chef_recipes = Table(
    "chef_recipes",
    Base.metadata,
    
    Column("chef_id", ForeignKey("chefs.id"), primary_key=True),
    Column("recipe_id", ForeignKey("recipes.id"), primary_key=True)
)

class Chef(Base):
    __tablename__ = "chefs"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    
    recipes: Mapped[list["Recipe"]] = relationship(secondary="chef_recipes", back_populates="chefs")


class Recipe(Base):
    __tablename__ = "recipes"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    ingredients: Mapped[str]
    
    chefs: Mapped[list["Chef"]] = relationship(secondary="chef_recipes", back_populates="recipes")



chef = Chef(name="Hilda Baci")
cake = Recipe(name="cake", ingredients="salt, sugar, flour, water")
rice = Recipe(name="Rice", ingredients="salt, water, oil")
beans = Recipe(name="Beans", ingredients="palm-oil, grounded-pepper, salt, maggi")

chef_2 = Chef(name="Ayo")

chef.recipes.append(cake)
chef.recipes.extend([rice, beans])

rice.chefs.append(chef_2)

print(chef.recipes)
print(rice.chefs)


# Every user_id must reference must reference a real user, this is called, referential integrity
