from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'QLthietbi_app'
urlpatterns = [
    path('dangnhap/', views.render_login, name='render_login'),
    path('login', views.perform_login, name='perform_login'),
    path('logout', views.perform_logout, name='perform_logout'),
    path('quanly/', views.render_trangchinh, name='render_trangchinh'),
    path('xoa_nhieuthietbi/', views.xoa_nhieuthietbi, name='xoa_nhieuthietbi'),
    path('themthietbi/', views.render_themthietbi, name='render_themthietbi'),
    path('<str:pk>/', views.render_capnhap, name='render_capnhap'),
    path('ajax/laythongtinphong/', views.load_phong, name='ajax_load_phong'),
   
    path('thietbi/<str:id_thiet_bi>', views.render_chitietthietbi, name='render_chitietthietbi'),
    path('chinhsuathietbi/<str:id_thiet_bi>', views.render_chinhsuathietbi, name='render_chinhsuathietbi'),
    path('xoathietbi/<str:id_thiet_bi>', views.render_xoathietbi, name='render_xoathietbi'),
    
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
