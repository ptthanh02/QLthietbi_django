# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from .models import NhanVien, MyUser

# class SignUpForm(UserCreationForm):
#     class Meta:
#         model = MyUser
#         fields = ('TENDANGNHAP', 'MATKHAU1', 'MATKHAU2', 'is_manager', 'is_techinician')
        
# class NhanVienForm(forms.ModelForm):
#     class Meta:
#         model = NhanVien
#         fields = ('HOTEN', 'GIOITINH', 'NGAYSINH', 'NGAYVAOLAM', 'CHUCVU', 'TRANGTHAI', 'MAIL', 'SDT', 'TENDANGNHAP', 'MATKHAU')
#         labels = {
#             'HOTEN': 'Họ tên',
#             'GIOITINH': 'Giới tính',
#             'NGAYSINH': 'Ngày sinh',
#             'NGAYVAOLAM': 'Ngày vào làm',
#             'CHUCVU': 'Chức vụ',
#             'TRANGTHAI': 'Trạng thái',
#             'MAIL': 'Mail',
#             'SDT': 'Số điện thoại',
#             'TENDANGNHAP': 'Tên đăng nhập',
#             'MATKHAU': 'Mật khẩu',
#         }
#         widgets = {
#             'HOTEN': forms.TextInput(attrs={'class': 'form-control'}),
#             'GIOITINH': forms.Select(attrs={'class': 'form-control'}),
#             'NGAYSINH': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#             'NGAYVAOLAM': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#             'CHUCVU': forms.Select(attrs={'class': 'form-control'}),
#             'TRANGTHAI': forms.Select(attrs={'class': 'form-control'}),
#             'MAIL': forms.TextInput(attrs={'class': 'form-control'}),
#             'SDT': forms.TextInput(attrs={'class': 'form-control'}),
#             'TENDANGNHAP': forms.TextInput(attrs={'class': 'form-control'}),
#             'MATKHAU': forms.TextInput(attrs={'class': 'form-control'}),
#         }
        
# class NhanVienUpdateForm(forms.ModelForm):
#     class Meta:
#         model = NhanVien
#         fields = ('HOTEN', 'GIOITINH', 'NGAYSINH', 'NGAYVAOLAM', 'CHUCVU', 'TRANGTHAI', 'MAIL', 'SDT')
#         labels = {
#             'HOTEN': 'Họ tên',
#             'GIOITINH': 'Giới tính',
#             'NGAYSINH': 'Ngày sinh',
#             'NGAYVAOLAM': 'Ngày vào làm',
#             'CHUCVU': 'Chức vụ',
#             'TRANGTHAI': 'Trạng thái',
#             'MAIL': 'Mail',
#             'SDT': 'Số điện thoại',
#         }
#         widgets = {
#             'HOTEN': forms.TextInput(attrs={'class': 'form-control'}),
#             'GIOITINH': forms.Select(attrs={'class': 'form-control'}),
#             'NGAYSINH': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#             'NGAYVAOLAM': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#             'CHUCVU': forms.Select(attrs={'class': 'form-control'}),
#             'TRANGTHAI': forms.Select(attrs={'class': 'form-control'}),
#             'MAIL': forms.TextInput(attrs={'class': 'form-control'}),
#             'SDT': forms.TextInput(attrs={'class': 'form-control'}),
#         }
        
# class NhanVienUpdatePasswordForm(forms.ModelForm):
#     class Meta:
#         model = NhanVien
#         fields = ('MATKHAU',)
#         labels = {
#             'MATKHAU': 'Mật khẩu',
#         }
#         widgets = {
#             'MATKHAU': forms.TextInput(attrs={'class': 'form-control'}),
#         }
        
# class NhanVienUpdateUsernameForm(forms.ModelForm):
#     class Meta:
#         model = NhanVien
#         fields = ('TENDANGNHAP',)
#         labels = {
#             'TENDANGNHAP': 'Tên đăng nhập',
#         }
#         widgets = {
#             'TENDANGNHAP': forms.TextInput(attrs={'class': 'form-control'}),
#         }
        
# class NhanVienUpdateRoleForm(forms.ModelForm):
#     class Meta:
#         model = NhanVien
#         fields = ('is_manager', 'is_techinician')
#         labels = {
#             'is_manager': 'Quản lý',
#             'is_techinician': 'Kỹ thuật viên',
#         }
#         widgets = {
#             'is_manager': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#             'is_techinician': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#         }
        
# class NhanVienUpdateStatusForm(forms.ModelForm):
#     class Meta:
#         model = NhanVien
#         fields = ('TRANGTHAI',)
#         labels = {
#             'TRANGTHAI': 'Trạng thái',
#         }
#         widgets = {
#             'TRANGTHAI': forms.Select(attrs={'class': 'form-control'}),
#         }
        
# class NhanVienUpdateRoleForm(forms.ModelForm):
#     class Meta:
#         model = NhanVien
#         fields = ('is_manager', 'is_techinician')
#         labels = {
#             'is_manager': 'Quản lý',
#             'is_techinician': 'Kỹ thuật viên',
#         }
#         widgets = {
#             'is_manager': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#             'is_techinician': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#         }

# # Path: QLthietbi_app\urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('nhanvien/', views.nhanvien, name='nhanvien'),
#     path('nhanvien/add/', views.nhanvien_add, name='nhanvien_add'),
#     path('nhanvien/update/<int:id>/', views.nhanvien_update, name='nhanvien_update'),
#     path('nhanvien/update_password/<int:id>/', views.nhanvien_update_password, name='nhanvien_update_password'),
#     path('nhanvien/update_username/<int:id>/', views.nhanvien_update_username, name='nhanvien_update_username'),
#     path('nhanvien/update_role/<int:id>/', views.nhanvien_update_role, name='nhanvien_update_role'),
#     path('nhanvien/update_status/<int:id>/', views.nhanvien_update_status, name='nhanvien_update_status'),
#     path('nhanvien/delete/<int:id>/', views.nhanvien_delete, name='nhanvien_delete'),
# ]

# # Path: QLthietbi_app\views.py
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth import update_session_auth_hash
# from django.contrib import messages
# from django.contrib.auth.decorators import user_passes_test
# from django.contrib.auth.decorators import permission_required
# from django.contrib.auth.decorators import login_required

# from .models import NhanVien
# from .forms import NhanVienForm, NhanVienUpdateForm, NhanVienUpdatePasswordForm, NhanVienUpdateUsernameForm, NhanVienUpdateRoleForm, NhanVienUpdateStatusForm

# @login_required(login_url='/login/')
# @user_passes_test(lambda u: u.is_superuser)
# def nhanvien(request):
#     nhanvien = NhanVien.objects.all()
#     return render(request, 'nhanvien.html', {'nhanvien': nhanvien})

# @login_required(login_url='/login/')
# @user_passes_test(lambda u: u.is_superuser)
# def nhanvien_add(request):
#     if request.method == 'POST':
#         form = NhanVienForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('nhanvien')
#     else:
#         form = NhanVienForm()
#     return render(request, 'nhanvien_add.html', {'form': form})

# @login_required(login_url='/login/')
# @user_passes_test(lambda u: u.is_superuser)
# def nhanvien_update(request, id):
#     nhanvien = NhanVien.objects.get(id=id)
#     if request.method == 'POST':
#         form = NhanVienUpdateForm(request.POST, instance=nhanvien)
#         if form.is_valid():
#             form.save()
#             return redirect('nhanvien')
#     else:
#         form = NhanVienUpdateForm(instance=nhanvien)
#     return render(request, 'nhanvien_update.html', {'form': form})

# @login_required(login_url='/login/')
# @user_passes_test(lambda u: u.is_superuser)

# def nhanvien_update_password(request, id):
#     nhanvien = NhanVien.objects.get(id=id)
#     if request.method == 'POST':
#         form = NhanVienUpdatePasswordForm(request.POST, instance=nhanvien)
#         if form.is_valid():
#             form.save()
#             return redirect('nhanvien')
#     else:
#         form = NhanVienUpdatePasswordForm(instance=nhanvien)
#     return render(request, 'nhanvien_update_password.html', {'form': form})

# @login_required(login_url='/login/')
# @user_passes_test(lambda u: u.is_superuser)
# def nhanvien_update_username(request, id):
#     nhanvien = NhanVien.objects.get(id=id)
#     if request.method == 'POST':
#         form = NhanVienUpdateUsernameForm(request.POST, instance=nhanvien)
#         if form.is_valid():
#             form.save()
#             return redirect('nhanvien')
#     else:
#         form = NhanVienUpdateUsernameForm(instance=nhanvien)
#     return render(request, 'nhanvien_update_username.html', {'form': form})

# @login_required(login_url='/login/')
# @user_passes_test(lambda u: u.is_superuser)
# def nhanvien_update_role(request, id):
#     nhanvien = NhanVien.objects.get(id=id)
#     if request.method == 'POST':
#         form = NhanVienUpdateRoleForm(request.POST, instance=nhanvien)
#         if form.is_valid():
#             form.save()
#             return redirect('nhanvien')
#     else:
#         form = NhanVienUpdateRoleForm(instance=nhanvien)
#     return render(request, 'nhanvien_update_role.html', {'form': form})

# @login_required(login_url='/login/')
# @user_passes_test(lambda u: u.is_superuser)
# def nhanvien_update_status(request, id):
#     nhanvien = NhanVien.objects.get(id=id)
#     if request.method == 'POST':
#         form = NhanVienUpdateStatusForm(request.POST, instance=nhanvien)
#         if form.is_valid():
#             form.save()
#             return redirect('nhanvien')
#     else:
#         form = NhanVienUpdateStatusForm(instance=nhanvien)
#     return render(request, 'nhanvien_update_status.html', {'form': form})

# @login_required(login_url='/login/')
# @user_passes_test(lambda u: u.is_superuser)
# def nhanvien_delete(request, id):
#     nhanvien = NhanVien.objects.get(id=id)
#     nhanvien.delete()
#     return redirect('nhanvien')