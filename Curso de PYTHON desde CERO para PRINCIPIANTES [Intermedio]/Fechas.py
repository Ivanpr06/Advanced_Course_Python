from datetime import datetime

ahora = datetime.now()

def print_date(fecha):
    print(fecha.year)
    print(fecha.month)
    print(fecha.day)
    print(fecha.hour)
    print(fecha.minute)
    print(fecha.second)
    print(fecha.timestamp())

def fecha_actual():
    print_date(ahora)

def crear_fecha():
    anyo_2026 = datetime(2026,7,9,12,50,30)
    print_date(anyo_2026)


from datetime import time

def tiempo_actual():
    tiempo_actual = time(7,50,40, 20)
    print(tiempo_actual.hour)
    print(tiempo_actual.minute)
    print(tiempo_actual.second)
    print(tiempo_actual.microsecond)


from _datetime import date
def current_date():
    current_date = date.today()
    print(current_date)

    current_date = date(2026,7,9)
    print(current_date)

    current_date = date(current_date.year + 1, current_date.month + 4, current_date.day + 14)
    print(current_date)


from datetime import timedelta

start_timedelta = timedelta(200, 10, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)

