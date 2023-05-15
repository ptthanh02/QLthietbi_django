from django import forms
from django.forms import ModelForm
from .models import *

# Tạo form thêm thiết bị
class ThemThietBiForm(ModelForm):
    class Meta:
        model = ThietBi
        fields = ('ten_thiet_bi','loai_thiet_bi', 'hinh_anh', 'mo_ta', 'ngay_mua', 'gia_mua', 'tinh_trang', 'phong')
        widgets = {
            'ten_thiet_bi': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nhập tên thiết bị'}),
            'loai_thiet_bi': forms.Select(attrs={'class': 'form-control'}),
            'ngay_mua': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gia_mua': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Nhập giá mua'}),
            'mo_ta': forms.Textarea(attrs={'class': 'form-control'}),
            'tinh_trang': forms.Select(attrs={'class': 'form-control'}),
            # 'tang': forms.Select(attrs={'class': 'form-control'}),
            'phong': forms.Select(attrs={'class': 'form-control'}),
        }

 