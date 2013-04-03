from django.db import models
from sorl.thumbnail import ImageField
from image_cropping import ImageRatioField, ImageCropField

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

    def thumbnail_url(self):
        return "http://img.youtube.com/vi/%s/0.jpg" % self.video_code
    def youtube_url(self):
        return "http://youtube.com/watch?v=%s" % self.video_code

    def __unicode__(self):
        return u"%s %s" % (self.title, self.pub_date)

class Participant(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_number = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=16)
    email = models.EmailField(max_length=64)
    tshirt_size = models.CharField(max_length=8)
    cap_size = models.CharField(max_length=8)
    camp_variant = models.CharField(max_length=8)
    transfer = models.CharField(max_length=8)

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)

class Message(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=16, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField()

    def __unicode__(self):
        return u"%s %s" % (self.subject, self.pub_date)

# Email
from django.template import Template, Context
from django.core.mail import send_mail

class Email(models.Model):
    id_name = models.CharField(max_length=255)
    default_sender = models.EmailField(max_length=255)
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
