from django.contrib import admin
from .models import user
admin.site.register(user)
# Register your models here.
from .models import logi
admin.site.register(logi)

# from .models import shop
# admin.site.register(shop)

from .models import price
admin.site.register(price)

from .models import employee
admin.site.register(employee)

from .models import detail
admin.site.register(detail)

from .models import orders
admin.site.register(orders)

from .models import cancel
admin.site.register(cancel)

from .models import concent
admin.site.register(concent)

from .models import product
admin.site.register(product)

