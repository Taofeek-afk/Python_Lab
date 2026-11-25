from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship

Base = declarative_base()

class ChefRecipe(Base):
    __tablename__ = "chef_recipes"
    
    # id: Mapped[int] = mapped_column(primary_key=True)
    chef_id: Mapped[int] = mapped_column(ForeignKey("chefs.id"), primary_key=True)
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipes.id"), primary_key=True)
    rating: Mapped[int]
    
    recipe: Mapped["Recipe"] = relationship(back_populates="chef_recipes")
    chef: Mapped["Chef"] = relationship(back_populates="chef_recipes")


class Chef(Base):
    __tablename__ = "chefs"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    
    chef_recipes: Mapped[list["ChefRecipe"]] = relationship(back_populates="chef")


class Recipe(Base):
    __tablename__ = "recipes"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    ingredients: Mapped[str]
    
    chef_recipes: Mapped[list["ChefRecipe"]] = relationship(back_populates="recipe")

chef = Chef(name="Hilda Baci")
recipe = Recipe(name="bread", ingredients="flour, salt, sugar, oil, water, flavour")
chef_recipe = ChefRecipe(rating=8)

chef_recipe.chef = chef
chef_recipe.recipe = recipe

print(chef_recipe.chef.name)
print(chef_recipe.recipe.chef)
print(chef_recipe.rating)

print(chef.chef_recipes)
print(recipe.chef_recipes)

# Every user_id must reference must reference a real user, this is called, referential integrity
