import time
from pprint import pprint

from django.contrib import admin
from . import sync
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    exclude = ('custom_key',)
    actions = ['delete_selected']
    def save_model(self, request, obj, form, change):
        command = 'PUT'
        if obj.custom_key < 0:
            command = 'POST'
            obj.custom_key = int(time.time()*(10**4))

        pprint(obj)
        super().save_model(request, obj, form, change)
        sync.sync_db(obj, command)

    def delete_model(self, request, obj):
        print("Deleting")
        sync.sync_db(obj, 'DELETE')
        super().delete_model(request, obj)

    def delete_selected(self, request, obj):
        for o in obj.all():
            sync.sync_db(o, 'DELETE')
            o.delete()
