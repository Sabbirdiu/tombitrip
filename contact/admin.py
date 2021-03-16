from django.contrib import admin
from .models import Faq,Contact,Traveller,Ownercamper,Ownercaravan,Ownerquote
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name',  'email', 'contact_date')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'email', )
  list_per_page = 25

admin.site.register(Contact,ContactAdmin)
admin.site.register(Faq)
admin.site.register(Traveller)
admin.site.register(Ownercamper)
admin.site.register(Ownercaravan)
admin.site.register(Ownerquote)