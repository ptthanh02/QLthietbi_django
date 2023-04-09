from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'ho', 'ten', 'gioi_tinh', 'chuc_vu', 'ngay_sinh', 'email', 'sdt', 'ngay_vao_lam', 'is_staff', 'is_active')
    list_filter = ('chuc_vu', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Thông tin cá nhân', {'fields': ('ho', 'ten', 'gioi_tinh', 'chuc_vu', 'ngay_sinh', 'email', 'sdt', 'ngay_vao_lam')}),
        ('Quyền hạn', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'ho', 'ten', 'password1', 'password2', 'sdt', 'gioi_tinh', 'ngay_sinh', 'chuc_vu', 'is_active', 'is_staff')}
        ),
    )
    search_fields = ('username', 'email', 'ho', 'ten')
    ordering = ('username',)
    


admin.site.register(CustomUser, CustomUserAdmin)




