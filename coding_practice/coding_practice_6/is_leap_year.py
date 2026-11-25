def is_leap_year(year: int = 2023) -> str:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return f"{year} -> {year} is a leap year"
    
    return f"{year} -> {year} is not a leap year"

print(is_leap_year())
