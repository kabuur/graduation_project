from django.contrib import admin
from .models import  Patient,NormalPN,NormalTB,Tuberculosis,Pneumonia
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.


# class customUserAdmin(UserAdmin):
#     addForm = UserCreationForm
#     form = UserChangeForm
#     model = customUser
#     list_display = ['pk','email','username','first_name','last_name']
#     add_fieldsets = UserAdmin.add_fieldsets+(
#         (None,{'fields':('email','first_name','last_name')})
#     )
#     fields = UserAdmin.fieldsets
# admin.site.register(customUser,customUserAdmin)



admin.site.register(Patient),
admin.site.register(Pneumonia),
admin.site.register(Tuberculosis),
admin.site.register(NormalTB),
admin.site.register(NormalPN),