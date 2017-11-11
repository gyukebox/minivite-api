from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(PollModel)
admin.site.register(SelectionModel)
admin.site.register(ResultModel)