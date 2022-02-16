from django.contrib import admin
from home.models import contacts

# Register your models here.
class contactsAdmin(admin.ModelAdmin):
    pass
admin.site.register(contacts, contactsAdmin)



#python manage.py createsuperuser [after admin registry]
#open admin page on localhost/admin