from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import Post

User=get_user_model()
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields=['eamil']
    form=UserAdminChangeForm
    add_form =UserAdminCreationForm

    
admin.site.register(User, UserAdmin)
admin.site.register(Post)