from django.contrib import admin
from test_models.models import *
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Passport)
admin.site.register(Person)
admin.site.register(Student)
admin.site.register(Teacher)