from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(StudentInfo)
admin.site.register(Stu_Question)
admin.site.register(StuExam_DB)
admin.site.register(StuResults_DB)