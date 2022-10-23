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
    now = datetime.date.today()
    time_served = now - start_of_service
    end_of_service = datetime.date.fromisoformat("2023-06-18")
    days_left = end_of_service - now
    percent = time_served / (end_of_service - start_of_service)
    html = f'<p>It is {now}</p>'
    html += f'<p>You started mil service on {start_of_service}</p>'
    html += f'<p>You have been serving the damn country for {time_served.days} days</p>'
    html += f'<p>Your service ends on {end_of_service}</p>'
    html += f'<p>That leaves {days_left.days} days of service left</p>'
    html += f'<p>You are {percent * 100:.02f}% done with this shithole</p>'
    context = {

    }

    return HttpResponse(html)
