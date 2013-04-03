from django.contrib import admin
from models import New, Video, Participant, Message, Email
from sorl.thumbnail.admin import AdminImageMixin
from image_cropping import ImageCroppingMixin

class NewAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "birth_number", "address", "phone",
        "email", "tshirt_size", "cap_size", "camp_variant", "transfer")

admin.site.register(New, NewAdmin)
admin.site.register(Video)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Message)
admin.site.register(Email)