from django.contrib import admin
from .models import User, trolling,City,products,cart,boat,fishermen

# Register your models here.
admin.site.register(User),
admin.site.register(trolling),
admin.site.register(City),
admin.site.register(products),
admin.site.register(cart),
admin.site.register(boat),
admin.site.register(fishermen)



