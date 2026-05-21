from django.contrib import admin
from .models import rackets , racket_reviews , racket_type , LaserSerial 

# Register your models here.
class racket_reviewsInLine(admin.TabularInline):
    model = racket_reviews
    extra = 1


class racketsAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'pricing', 'date_added')
    inlines = [racket_reviewsInLine]
    
class racket_typeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    filter_horizontal = ('rackets',)

class LaserSerialAdmin(admin.ModelAdmin):
    list_display = ('serial_code', 'racket', 'warranty_months')
    search_fields = ('serial_code', 'racket__name')


admin.site.register(rackets, racketsAdmin)
admin.site.register(racket_type, racket_typeAdmin)
admin.site.register(LaserSerial, LaserSerialAdmin)