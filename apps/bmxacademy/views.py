# coding: utf8
import json
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

from models import New, Video, Email, Gallery
from forms import RegistrationForm, MessageForm

from helpers import show_intro, registration_form_process, contact_form_process

def index_view(request, template="bmxacademy/index.html"):
    if show_intro(request):
        return HttpResponseRedirect("/intro/")

    new_qs = New.objects.order_by("-pk")
    video_qs = Video.objects.order_by("-pk")
    gallery_qs = Gallery.objects.order_by("-pk")
    registration_form_done = False
    message_form_done  = False

    registration_form = RegistrationForm(request.POST or None, prefix="registration")
    if registration_form.is_valid():
        obj = registration_form.save()
        d = { "name": obj.name, "email": obj.email, "phone": obj.phone, }
        Email.objects.get(id_name="registration").send(settings.NOTIFY_MAIL, d)
        Email.objects.get(id_name="registration_participant").send(obj.email, d)
        registration_form_done = True
        # return HttpResponseRedirect("/")

    message_form = MessageForm(request.POST or None, prefix="message")
    if message_form.is_valid():
        obj = message_form.save()
        d = {"text": obj.text, "name": obj.name, "phone": obj.phone, "email": obj.email, "subject": obj.subject, }
        Email.objects.get(id_name="message").send(settings.NOTIFY_MAIL, d, obj.email)
        message_form_done = True
        # return HttpResponseRedirect("/")

    if not request.POST:
        registration_form = None
        message_form = None
    else:
        if request.POST["form"] == "message":
            registration_form = None
        if request.POST["form"] == "registration":
            message_form = None

    a = gallery_qs[0].picture_set.order_by("order")[:300]
    gallery = [a[i:i+12] for i in range(0,len(a),12)]
    return render_to_response(template, 
        {
            "new_qs": new_qs,
            "video_qs": video_qs,
            "registration_form": registration_form,
            "message_form": message_form,
            "gallery_qs": gallery_qs,
            "gallery": gallery,
            "registration_form_done": registration_form_done,
            "message_form_done": message_form_done,
        },
        context_instance=RequestContext(request))

from easy_thumbnails.files import get_thumbnailer
def gallery_json(request, gallery_pk):
    gallery = Gallery.objects.get(pk=gallery_pk)
    out = []
    for picture in gallery.picture_set.all():
        thumbnail_url = get_thumbnailer(picture.img).get_thumbnail({'size': (430, 360), 'box': picture.img_crop, 'crop': True, 'detail': True, }).url
        out.append({
            "thumbnail": thumbnail_url,
            "full": picture.img.url,
        })
    response = json.dumps(out)
    return HttpResponse(response, mimetype="application/json")



def intro_view(request, template="bmxacademy/intro.html"):
    return render_to_response(template, 
        {
        },
        context_instance=RequestContext(request))

def contact_view(request, template="bmxacademy/contact.html"):
    registration_form_done, registration_form = registration_form_process(request)
    message_form_done, message_form = contact_form_process(request)
    
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
            "message_form": message_form,
            "message_form_done": message_form_done,
        },
        context_instance=RequestContext(request))

def registration_view(request, template="bmxacademy/register.html"):
    registration_form_done, registration_form = registration_form_process(request)
    message_form_done, message_form = contact_form_process(request)

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
            "registration_form": registration_form,
            "registration_form_done": registration_form_done,
        },
        context_instance=RequestContext(request))
