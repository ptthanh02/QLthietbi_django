from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'QLthietbi_app'
urlpatterns = [
    path('dangnhap/', views.render_login, name='render_login'),
    path('login', views.perform_login, name='perform_login'),
    path('logout', views.perform_logout, name='perform_logout'),
    path('quanly/', views.ThietBi_view.as_view(), name='render_trangchinh'),
    path('tao_file.txt/', views.tao_file_txt, name='tao_file_txt'),
    path('tao_file.csv/', views.tao_file_csv, name='tao_file_csv'),
    path('vitri/', views.render_vitri_thietbi, name='render_vitri_thietbi'),
    path('xoa_loai_thiet_bi/<int:pk>', views.xoa_loai_thiet_bi, name='xoa_loai_thiet_bi'),
    path('xoa_phong/<int:pk>', views.xoa_phong, name='xoa_phong'),
    path('xoa_tang/<int:pk>', views.xoa_tang, name='xoa_tang'),
    path('them_loai_thiet_bi/', views.them_loai_thiet_bi, name='them_loai_thiet_bi'),
    path('them_phong/', views.them_phong, name='them_phong'),
    path('them_tang/', views.them_tang, name='them_tang'),
    
    path('themthietbi/', views.render_themthietbi, name='render_themthietbi'),
    path('<str:pk>/', views.render_capnhap, name='render_capnhap'), # cập nhập thông tin thiết bị lúc thay đổi phòng
    path('ajax/laythongtinphong/', views.load_phong, name='ajax_load_phong'),
    
    path('thietbi/<str:id_thiet_bi>', views.render_chitietthietbi, name='render_chitietthietbi'),
    path('chinhsuathietbi/<str:id_thiet_bi>', views.render_chinhsuathietbi, name='render_chinhsuathietbi'),
    path('xoathietbi/<str:id_thiet_bi>', views.render_xoathietbi, name='render_xoathietbi'),
    path('xoanhieu/', views.ThietBi_view.as_view(), name='xoa_nhieu'),
    
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
