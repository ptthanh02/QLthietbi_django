from django import forms
from django.forms import ModelForm
from .models import *

class ThemThietBiForm(forms.ModelForm):
    
    class Meta:
        model = ThietBi
        fields = ('ten_thiet_bi', 'loai_thiet_bi', 'hinh_anh', 'mo_ta', 'ngay_mua', 'gia_mua', 'tinh_trang', 'tang', 'phong')
        widgets = {
            'ten_thiet_bi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập tên thiết bị'}),
            'loai_thiet_bi': forms.Select(attrs={'class': 'form-control'}),
            'ngay_mua': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gia_mua': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nhập giá mua'}),
            'mo_ta': forms.Textarea(attrs={'class': 'form-control'}),
            'tinh_trang': forms.Select(attrs={'class': 'form-control'}),
            'tang': forms.Select(attrs={'class': 'form-control', 'name': 'tang'}),
            'phong': forms.Select(attrs={'class': 'form-control', 'name': 'phong'}),
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
    
