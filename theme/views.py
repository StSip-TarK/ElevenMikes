from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime

""" def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
 """


def index(request):
    start_of_service = datetime.date.fromisoformat("2022-07-18")
    end_of_service = datetime.date.fromisoformat("2023-06-18")
    now = datetime.date.today()
    time_served = now - start_of_service
    days_left = (end_of_service - now).days
    percent = time_served / (end_of_service - start_of_service)

    context = {
        "start": start_of_service,
        "now": now,
        "served": time_served.days,
        "end": end_of_service,
        "left": days_left,
        "percent": f"{percent * 100:.02f}",
    }

    return render(request, 'index.html', context)
