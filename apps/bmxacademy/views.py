# coding: utf8
import jsonindex
from django.conf import settings
import os
normpath = lambda *args: os.path.normpath(os.path.abspath(os.path.join(*args)))
PROJECT_ROOT = settings.PROJECT_ROOT

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

from models import New, Video, Email
from forms import RegistrationForm, MessageForm

def index_view(request, template="bmxacademy/index.html"):
    new_qs = New.objects.order_by("-pk")
    video_qs = Video.objects.order_by("-pk")

    registration_form = RegistrationForm(request.POST or None, prefix="registration")
    if registration_form.is_valid():
        obj = registration_form.save()
        d = { "first_name": obj.first_name, "last_name": obj.last_name, "email": obj.email, "phone": obj.phone, }
        Email.objects.get(id_name="registration").send(settings.NOTIFY_MAIL, d)
        Email.objects.get(id_name="registration_participant").send(obj.email, d)
        return HttpResponseRedirect("/")

    message_form = MessageForm(request.POST or None, prefix="message")
    if message_form.is_valid():
        obj = message_form.save()
        d = {"text": obj.text, "name": obj.name, "phone": obj.phone, "email": obj.email, "subject": obj.subject, }
        Email.objects.get(id_name="message").send(settings.NOTIFY_MAIL, d, obj.email)
        return HttpResponseRedirect("/")

    if not request.POST:
        registration_form = None
        message_form = None
    else:
        if request.POST["form"] == "message":
            registration_form = None
        if request.POST["form"] == "registration":
            message_form = None

    return render_to_response(template, 
        {
            "new_qs": new_qs,
            "video_qs": video_qs,
            "registration_form": registration_form,
            "message_form": message_form,
        },
        context_instance=RequestContext(request))

def images_json(request):
    srv = normpath(PROJECT_ROOT, "static", "static", "images")
    www = normpath(PROJECT_ROOT)
    response = jsonindex.index(srv, www)
    return HttpResponse(response, mimetype="application/json")