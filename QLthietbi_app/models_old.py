from django.db import models
from datetime import datetime
from django.db.models import Max
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
from django.db.models.signals import post_save

class User(AbstractUser):
    class CHUCVU(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin', 'admin'
        QUANLY = 'Quản lý', 'quản lý', 'quanly', 'Quanly', 'Quan ly', 'quan ly'
        NHANVIEN = 'Nhân viên', 'nhân viên', 'nhanvien', 'NhanVien', 'Nhan Vien', 'nhan vien'
        KYTHUATVIEN = 'Kỹ thuật viên', 'kỹ thuật viên', 'kythuatvien', 'KyThuatVien', 'Ky thuat vien', 'ky thuat vien'
    
    base_role = CHUCVU.ADMIN
    chucvu = models.CharField(max_length=50, choices=CHUCVU.choices, default=CHUCVU.ADMIN)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.chucvu = self.base_role 
        super(User, self).save(*args, **kwargs)
    
    
class Tang(models.Model):
    MATANG = models.CharField(max_length=10, primary_key=True)
    SOTANG = models.IntegerField()

    def __str__(self):
        return self.MATANG

class Phong(models.Model):
    MATANG = models.ForeignKey(Tang, on_delete=models.CASCADE)
    MAPHONG = models.CharField(max_length=10, primary_key=True)
    SOPHONG = models.IntegerField()

    def __str__(self):
        return self.MAPHONG

class ThietBi(models.Model):
    MATB = models.CharField(max_length=20, primary_key=True)
    TENTB = models.CharField(max_length=50)
    LOAI = models.CharField(max_length=50)
    HINHANH = models.ImageField(upload_to='images/', blank=True)
    NGAYMUA = models.DateField(null=True)
    GIAMUA = models.IntegerField()
    TINHTRANG = models.CharField(max_length=50)
    THONGTIN = models.CharField(max_length=300)
    NGAYBAOTRI = models.DateField(null=True)
    MAPHONG = models.ForeignKey(Phong, on_delete=models.CASCADE)
    MATANG = models.ForeignKey(Tang, on_delete=models.CASCADE)

    def __str__(self):
        return self.MATB

# class NhanVien(models.Model):
#     MANV = models.CharField(max_length=10, primary_key=True, blank=True, null=False, unique=True, editable=False)
#     HOTEN = models.CharField(max_length=50)
#     GIOITINH = models.BooleanField(default=True)
#     NGAYSINH = models.DateField()
#     NGAYVAOLAM = models.DateField()
#     TRANGTHAI = models.CharField(max_length=50)
#     MAIL = models.EmailField()
#     SDT = models.CharField(max_length=50)
#     TENDANGNHAP = models.CharField(max_length=50, null=False, blank=False, unique=True)
#     MATKHAU = models.CharField(max_length=50)
    
#     def save(self, *args, **kwargs):
#         if not self.MANV:
#             self.MANV = NhanVien.objects.aggregate(Max('MANV'))['MANV__max']
#             if self.MANV:
#                 self.MANV = 'NV' + str(int(self.MANV[2:]) + 1).zfill(4)
#             else:
#                 self.MANV = 'NV0001'
#         super(NhanVien, self).save(*args, **kwargs)
        
#     class Meta:
#         ordering = ['-MANV']
    
#     def __str__(self):
#         return self.MANV
    
# class MyUserManager(BaseUserManager):
#     def create_user(self, TENDANGNHAP, MATKHAU=None, **extra_fields):
#         if not TENDANGNHAP:
#             raise ValueError('Người dùng phải có tên đăng nhập')
#         user = self.model(TENDANGNHAP=TENDANGNHAP, **extra_fields)
#         user.set_password(MATKHAU)
#         user.save(using=self._db)
#         return user
    
#     def create_superuser(self, TENDANGNHAP, MATKHAU, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser phải có is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser phải có is_superuser=True.')

#         user = self.create_user(TENDANGNHAP=TENDANGNHAP, MATKHAU=MATKHAU, **extra_fields)

#         nhanvien = NhanVien.objects.get(TENDANGNHAP=TENDANGNHAP)
#         if nhanvien.CHUCVU == 'Quản lý':
#             user.is_manager = True
#             user.is_staff = True

#         user.save(using=self._db)

#         return user
    
# class MyUser(AbstractBaseUser, PermissionsMixin):
#     TENDANGNHAP = models.CharField(max_length=50, unique=True)
#     MATKHAU = models.CharField(max_length=50)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
    
#     objects = MyUserManager()
    
#     USERNAME_FIELD = 'TENDANGNHAP'
    
#     def save(self, *args, **kwargs):
#         if self.is_manager:
#             self.is_staff = True
#         super(MyUser, self).save(*args, **kwargs)
    
#     def __str__(self):
#         return self.TENDANGNHAP
