from django.contrib import admin
from inputform.models import UserName, UserEmail

admin.site.register(UserName)
admin.site.register(UserEmail)

list_display = [UserName.file_link,]