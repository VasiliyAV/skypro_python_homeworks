def month_to_season(month):
    if month in (12,1,2):
        print('Zima')
    elif month in (3,4,5):
        print('Vesna')
    elif month in (6,7,8):
        print('Leto')
    elif month in (9,10,11):
        print("Osen'")
    else:
        print('Введено неверное значение!')

month_to_season(12),month_to_season(1),month_to_season(2)
month_to_season(3),month_to_season(4),month_to_season(5)
month_to_season(6),month_to_season(7),month_to_season(8)
month_to_season(9),month_to_season(10),month_to_season(11)
month_to_season(13)
month_to_season('asd')
month_to_season(-1)