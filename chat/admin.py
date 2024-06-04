from django.contrib import admin
from .models import *

admin.site.register(ChatMessage)

class ChatMessageInline(admin.TabularInline):
    model = ChatMessage

class ThreadAdmin(admin.ModelAdmin):
    inlines = [ChatMessageInline]

admin.site.register(Thread, ThreadAdmin)