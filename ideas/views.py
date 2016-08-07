import datetime
from django.shortcuts import render
from models import *

def export_year(request):
	ideas = Idea.objects.filter(datetime__gte=datetime.datetime.now() - datetime.timedelta(days=365))
	return render(request, 'export_year.html', {
        'ideas': ideas,
    })
