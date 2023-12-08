from django.contrib import admin
from .models import JWData
# Register your models here.
class JWDataAdmin(admin.ModelAdmin):
    list_display=('id','Date','TradeCode','High','Low','Open','Close','Volume')

   

admin.site.register(JWData,JWDataAdmin)