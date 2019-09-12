from django.contrib import admin

from learning_logs.models import Topic, Entry
# Register your models here.
#Create models to show within the webpage
admin.site.register(Topic)
admin.site.register(Entry)

#page 440