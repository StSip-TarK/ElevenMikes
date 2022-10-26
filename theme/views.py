from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import date, timedelta
from .models import Course

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

    # courses
    all_courses = Course.objects.all()
    print(all_courses)

    weeks = []
    monday = start_of_service
    current_course = all_courses[0]
    for m in range(12):
        month = []
        for w in range(4):
            done = None
            if monday < date.today() < (monday + timedelta(days=7)):
                done = 100* (date.today().weekday()+1) / 7
            elif monday < date.today():
                done = 100
            else:
                done = 0
            
            for c in all_courses:
                if c.start_date < monday < c.end_date:
                  current_course = c

            month += [{
                'date': monday.strftime("%b %d"),
                'month': monday.strftime("%b"),
                'monday_day': monday.strftime("%d"),
                'percent': done,
                'course': current_course.abr_name
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
