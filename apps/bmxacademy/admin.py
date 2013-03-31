from django.contrib import admin
from models import New, Video, Participant
from sorl.thumbnail.admin import AdminImageMixin

class NewAdmin(AdminImageMixin, admin.ModelAdmin):
    pass

admin.site.register(New, NewAdmin)
admin.site.register(Video)
admin.site.register(Participant)