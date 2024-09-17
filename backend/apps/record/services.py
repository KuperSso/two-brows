from .models import Record


def get_booked_dates():     #Возвращает забронированные даты из БД в строковом формате

    dates = []
    for date in Record.objects.values("date_time").filter():
        dates.append(str(date["date_time"].date()))
    return dates

