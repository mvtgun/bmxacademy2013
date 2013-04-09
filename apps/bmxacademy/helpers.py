from models import Intro
from forms import RegistrationForm, MessageForm
from models import New, Video, Email, Gallery
import settings

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def show_intro(request):
    count = Intro.objects.all().count()
    Intro(ip=get_client_ip(request)).save()
    if count == 0:
        return True
    return False


def registration_form_process(request):
    registration_form_done = False
    registration_form = RegistrationForm(request.POST or None, prefix="registration")
    if registration_form.is_valid():
        obj = registration_form.save()
        d = { "name": obj.name, "email": obj.email, "phone": obj.phone, }
        Email.objects.get(id_name="registration").send(settings.NOTIFY_MAIL, d)
        Email.objects.get(id_name="registration_participant").send(obj.email, d)
        registration_form_done = True
        # return HttpResponseRedirect("/")
        registration_form = None
    return registration_form_done, registration_form

def contact_form_process(request):
    contact_form_done = False
    message_form = MessageForm(request.POST or None, prefix="message")
    if message_form.is_valid():
        obj = message_form.save()
        d = {"text": obj.text, "name": obj.name, "phone": obj.phone, "email": obj.email, "subject": obj.subject, }
        Email.objects.get(id_name="message").send(settings.NOTIFY_MAIL, d, obj.email)
        contact_form_done = True
        message_form = None
        # return HttpResponseRedirect("/")
    return contact_form_done, message_form