from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import date, timedelta

""" def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
 """


def index(request):
    start_of_service = date(2022, 7, 18)
    end_of_service = date(2023, 6, 18)
    now = date.today()
    time_served = now - start_of_service
    days_left = (end_of_service - now).days
    percent = time_served / (end_of_service - start_of_service)

    SBK = (date(2022, 7, 18), date(2022, 9, 11))
    NABK = (date(2022, 9, 12), date(2022, 10, 23))
    NAEK = (date(2022, 10, 24), date(2022, 12, 2))
    Holiday = (date(2022, 12, 19), date(2023, 1, 1))

    weeks = []
    monday = start_of_service
    for m in range(11):
        month = []
        for w in range(4):
            done = None
            if monday < date.today() < (monday + timedelta(days=7)):
                done = 100* (date.today().weekday()+1) / 7
            elif monday < date.today():
                done = 100
            else:
                done = 0
            


            month += [{
                'date': monday,
                'percent': done
            }]
            monday += timedelta(days=7)

        weeks += [month]
    print(weeks)

    context = {
        "start": start_of_service,
        "now": now,
        "served": time_served.days,
        "end": end_of_service,
        "left": days_left,
        "percent": f"{percent * 100:.01f}",
        "weeks": weeks,
        "totalDays": (end_of_service - start_of_service).days
    }

    return render(request, 'index.html', context)
