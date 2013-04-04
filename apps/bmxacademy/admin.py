from django.contrib import admin
from models import New, Video, Participant, Message, Email, Gallery, Picture
from sorl.thumbnail.admin import AdminImageMixin
from image_cropping import ImageCroppingMixin

class NewAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "registration_date", "birth_number", "address", "phone",
        "email", "tshirt_size", "cap_size", "camp_variant", "transfer", "advance", "payment")
    readonly_fields = ("registration_date", )

class PictureInline(admin.TabularInline):
    model = Picture
    extra = 0 

class GalleryAdmin(ImageCroppingMixin, admin.ModelAdmin):
    inlines = (PictureInline, )

class PictureAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(New, NewAdmin)
admin.site.register(Video)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Message)
admin.site.register(Email)