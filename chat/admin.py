from django.contrib import admin

from chat.models import Chat, Message

class MessageAdmin(admin.ModelAdmin):
    fields = ('text', 'created_at', 'chat', 'author', 'receiver')
    list_display = ('text', 'created_at', 'chat', 'author', 'receiver')

# Register your models here.
admin.site.register(Chat)
admin.site.register(Message, MessageAdmin)