from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

from models import New, Video
from forms import RegistrationForm

def index_view(request, template="bmxacademy/index.html"):
    new_qs = New.objects.order_by("-pk")
    video_qs = Video.objects.order_by("-pk")

    registration_form = RegistrationForm(request.POST or None, prefix="registration")
    if registration_form.is_valid():
        registration_form.save()
        
    if not request.POST:
        registration_form = False

    return render_to_response(template, 
        {
            "new_qs": new_qs,
            "video_qs": video_qs,
            "registration_form": registration_form,
        },
        context_instance=RequestContext(request))