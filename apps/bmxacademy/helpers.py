from models import Intro

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