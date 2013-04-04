import os

from django.core.files import File

from models import Picture, Gallery

normpath = lambda *args: os.path.normpath(os.path.abspath(os.path.join(*args)))

def picture_upload(path, gallery):
    f = File(open(path, 'r'))
    p = Picture(img=f, gallery=gallery)
    name = os.path.split(path)[1]
    p.img.save(name, f)
    p.save()

def main_2012(directory):
    for f in os.listdir(normpath(directory)):
        if f in (".", ".."):
            continue
        picture_upload(normpath(directory, f), Gallery.objects.get(pk=1))