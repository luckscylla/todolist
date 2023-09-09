from django.db import models
from django.contrib import admin

class Item(models.Model):
    content = models.TextField()
    done = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.content

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'done', 'date')
    list_filter = ('done','date')
    search_fields = ('content',)
    ordering = ('-id',)

