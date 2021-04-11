from django.contrib import admin
from .models import Administrator
from .models import Camp
from .models import Campclass
from .models import Course
from .models import Coursebystander
from .models import User
from .models import Campsignup
from .models import Campattend
from .models import Userdata
from .models import Usercompany
from .models import Activity
from .models import Activitytakes
from .models import Coursefile

# Register your models here.
admin.site.register(Administrator)
admin.site.register(Camp)
admin.site.register(Campclass)
admin.site.register(Course)
admin.site.register(Coursebystander)
admin.site.register(Campsignup)
admin.site.register(Campattend)
admin.site.register(User)
admin.site.register(Userdata)
admin.site.register(Usercompany)
admin.site.register(Activity)
admin.site.register(Activitytakes)
admin.site.register(Coursefile)
