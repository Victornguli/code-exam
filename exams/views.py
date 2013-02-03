from django.shortcuts import render_to_response
from django.template import RequestContext

def homepage(request):
    context = RequestContext(request)
    return render_to_response('exams/index.html', context)