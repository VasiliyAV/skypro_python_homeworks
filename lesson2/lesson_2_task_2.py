def is_year_leap(year):
    year = int(year)
    if year % 4 == 0:
        print(f"Год {year} високосный: True")
    else:
        print(f"Год {year} високосный: False")
    
is_year_leap(2023)
