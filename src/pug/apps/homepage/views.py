from django.conf import settings
from django.template import RequestContext, loader
from django.http import HttpResponse
from datetime import datetime

def index(request):
  t = loader.get_template('index.html')
  # dict is where you can add in template variables
  c = RequestContext(request, { "currentdate": str(datetime.now()) })
  return HttpResponse(t.render(c))
