from django.db import models
from sorl.thumbnail import ImageField

class New(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = ImageField(upload_to="bmxacademy/new/img")

    def __unicode__(self):
        return u"%s %s" % (self.title, self.pub_date)

class Video(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    video_code = models.CharField(max_length=16)

    def __unicode__(self):
        return u"%s %s" % (self.title, self.pub_date)

# class Participant(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     birth_number = models.CharField(max_length=13)
#     address = models.CharField(max_length=255)
#     phone = models.CharField(max_length=16)
#     email = models.EmailField(max_length=64)
#     tshirt_size = models.CharField(max_length=8)
#     cap_size = models.CharField(max_length=8)
#     camp_variant = models.CharField(max_length=8)
#     transfer = models.CharField(max_length=8)