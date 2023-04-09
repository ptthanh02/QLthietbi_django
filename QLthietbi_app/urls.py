from django.urls import path
from . import views

app_name = 'QLthietbi_app'
urlpatterns = [
    path('login/', views.render_login, name='render_login'),
    path('login', views.perform_login, name='perform_login'),
    path('logout', views.perform_logout, name='perform_logout'),
    path('Trangchinh/', views.render_trangchinh, name='render_trangchinh'),
]
