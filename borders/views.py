import json

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

from borders.models import BordersMI

def view_map(request):
    c = RequestContext(request)
    return render(request, 'borders/mi/view_map.html', context_instance=c)

def borders_data(request):
    border_list = []
    for shape in BordersMI.objects.all():
	border_list.append(shape.geom.json)
    return HttpResponse(json.dumps(border_list), mimetype="application/json")

