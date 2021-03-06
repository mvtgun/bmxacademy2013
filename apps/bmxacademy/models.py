from django.db import models
from sorl.thumbnail import ImageField
from image_cropping import ImageRatioField, ImageCropField
import settings
import urllib
import os
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from sorl.thumbnail import get_thumbnail

normpath = settings.normpath

class Intro(models.Model):
    ip = models.IPAddressField()

    def __unicode__(self):
        return u"%s" % self.ip

class New(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = ImageCropField(upload_to="bmxacademy/new/img")
    img_crop = ImageRatioField('img', '321x244')

    def __unicode__(self):
        return u"%s %s" % (self.title, self.pub_date)

class Video(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    video_code = models.CharField(max_length=16)

    img = ImageCropField(upload_to="bmxacademy/video/img", null=True, blank=True)
    img_crop = ImageRatioField('img', '290x217')
    img_is_uploaded = models.BooleanField()

    def thumbnail_url(self):
        return "http://img.youtube.com/vi/%s/0.jpg" % self.video_code
    def youtube_url(self):
        return "http://youtube.com/watch?v=%s" % self.video_code

    def update_img(self):
        self.img_is_uploaded = True
        url = self.thumbnail_url()
        file_name = os.path.split(url)[1]
        path = normpath(settings.PROJECT_ROOT, "static/uploads/bmxacademy/video/img", file_name)
        urllib.urlretrieve(url, path)
        f = File(file(path, 'r'))
        self.img.save(file_name, f)

    def save(self):
        super(Video, self).save()
        if not self.img_is_uploaded:
            self.update_img()

    def __unicode__(self):
        return u"%s %s" % (self.title, self.pub_date)

CAP_SIZES = (
    ("1", "6 7/8 (obvod hlavy - 54,9cm)"),
    ("2", "7 (obvod hlavy - 55,8cm)"),
    ("3", "7 3/4 (obvod hlavy - 56,8cm)"),
    ("4", "7 3/8 (obvod hlavy - 57,7cm)"),
    ("5", "7 1/2 (obvod hlavy - 58,7cm)"),
    ("6", "7 1/4 (obvod hlavy - 59,6cm)"),
    ("7", "7 3/4 (obvod hlavy - 60,6cm)"),
    ("8", "7 3/8 (obvod hlavy - 61,5cm)"),
    ("9", "7 5/8 (obvod hlavy - 62,5cm)"),
    ("10","8 (obvod hlavy - 63,5cm)"),
)

class Participant(models.Model):
    registration_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    birth_number = models.CharField(max_length=13)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    phone = models.CharField(max_length=16)
    email = models.EmailField(max_length=64, unique=True)
    tshirt_size = models.CharField(max_length=8)
    cap_size = models.CharField(max_length=8, choices=CAP_SIZES)
    camp_variant = models.CharField(max_length=8)
    transfer = models.CharField(max_length=8)
    advance = models.BooleanField(verbose_name="Zaloha")
    payment = models.BooleanField(verbose_name="Platba")
    note = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"%s" % (self.name)

class Message(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=16, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField()

    def __unicode__(self):
        return u"%s %s" % (self.subject, self.pub_date)

class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return u"%s" % (self.name)


class Picture(models.Model):
    gallery = models.ForeignKey(Gallery)
    order = models.IntegerField(default=0)
    img = ImageCropField(upload_to="bmxacademy/picture/img")
    img_crop = ImageRatioField("img", "130x130")

    def __unicode__(self):
        return u"%s  %i" % (self.gallery.name, self.pk)

    def large(self):
        if self.img.width > self.img.height:
            return get_thumbnail(self.img, '800x500', crop='center', quality=99)
        return get_thumbnail(self.img, '500x800', crop='center', quality=99)

# Email
from django.template import Template, Context
from django.core.mail import send_mail

class Email(models.Model):
    id_name = models.CharField(max_length=255)
    default_sender = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def render(self, d={}):
        subject = Template(self.subject).render(Context(d))
        message = Template(self.message).render(Context(d))
        return (subject, message)

    def send(self, to, d={}, sender=None, fail_silently=True):
        if not sender:
            sender = self.default_sender
        if type(to) in (str, unicode):
            to = [to, ]
        subject, message = self.render(d)
        send_mail(subject, message, sender, to, fail_silently=fail_silently)

    def __unicode__(self):
        return self.subject
