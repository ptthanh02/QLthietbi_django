from django import forms
from django.forms import ModelForm
from .models import *
from datetime import date

class ThemThietBiForm(forms.ModelForm):
    
    class Meta:
        model = ThietBi
        fields = ('ten_thiet_bi', 'loai_thiet_bi', 'hinh_anh', 'mo_ta', 'ngay_mua', 'gia_mua', 'tinh_trang', 'tang', 'phong', 'don_vi_cung_cap')
        widgets = {
            'ten_thiet_bi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập tên thiết bị'}),
            'loai_thiet_bi': forms.Select(attrs={'class': 'form-control'}),
            'ngay_mua': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gia_mua': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nhập giá mua'}),
            'mo_ta': forms.Textarea(attrs={'class': 'form-control'}),
            'tinh_trang': forms.Select(attrs={'class': 'form-control'}),
            'tang': forms.Select(attrs={'class': 'form-control', 'name': 'tang'}),
            'phong': forms.Select(attrs={'class': 'form-control', 'name': 'phong'}),
            'don_vi_cung_cap': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập đơn vị cung cấp'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phong'].queryset = Phong.objects.none()
        
        if 'tang' in self.data:
            try:
                tang_id = int(self.data.get('tang'))
                self.fields['phong'].queryset = Phong.objects.filter(tang_id=tang_id).order_by('ten_phong')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['phong'].queryset = self.instance.tang.phong_set.order_by('ten_phong')
            
    def clean_gia_mua(self):
        gia_mua = self.cleaned_data.get('gia_mua')
        if gia_mua is not None and gia_mua < 0:
            raise forms.ValidationError("không được là số âm.")
        return gia_mua
    
    def clean_ngay_mua(self):
        ngay_mua = self.cleaned_data['ngay_mua']
        today = date.today()
        if ngay_mua > today:
            raise forms.ValidationError("không được lớn hơn ngày hiện tại.")
        return ngay_mua
    
class LoaiThietBiForm(forms.ModelForm):
        
        class Meta:
            model = LoaiThietBi
            fields = ('ten_loaithietbi',)
            widgets = {
                'ten_loaithietbi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập tên loại thiết bị'}),
            }
    
class TangForm(forms.ModelForm):
    
    class Meta:
        model = Tang
        fields = ('ten_tang',)
        widgets = {
            'ten_tang': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập tên tầng'}),
        }
        
class PhongForm(forms.ModelForm):
    
    class Meta:
        model = Phong
        fields = ('ten_phong', 'tang')
        widgets = {
            'ten_phong': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập tên phòng'}),
            'tang': forms.Select(attrs={'class': 'form-control'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phong'].queryset = Phong.objects.none()
        
        if 'tang' in self.data:
            try:
                tang_id = int(self.data.get('tang'))
                self.fields['phong'].queryset = Phong.objects.filter(tang_id=tang_id).order_by('ten_phong')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['phong'].queryset = self.instance.tang.phong_set.order_by('ten_phong')