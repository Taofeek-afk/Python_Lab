import asyncio

from database import init_db


async def main():
    await init_db()


if __name__ == "__main__":
    asyncio.run(main())


# __all__ is a special variable in Python module files (like __init__.py) that explicitly defines what gets imported when someone runs from module import *.
    
import sqlite3

connection = sqlite3.connect("restaurant.db")

tables = connection.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    ORDER BY name;
""").fetchall()

for table in tables:
    print(table[0])

connection.close()
