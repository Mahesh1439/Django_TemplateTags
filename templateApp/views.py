from django.shortcuts import render
import datetime
# Create your views here.
def templatetags(request):
    date=datetime.datetime.now()
    week_days={"sunday":1,
               "monday":2,
               "tuesday":3,
               "wednesday":4,
               "thursday":5,
               "friday":6,
               "saturday":7
               }
    return render(request,f'template_html_files\\week_days.html',context=week_days)
