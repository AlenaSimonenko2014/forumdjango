from django.contrib import admin
from forum.models import Section, Topic, Message

# Register your models here.
admin.site.register(Section)
admin.site.register(Topic)
admin.site.register(Message)