from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Phong, ThietBi, LoaiThietBi
from .forms import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def render_login(request):
    return render(request, 'dangnhap.html')

def perform_login(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        rememberMe = request.POST.get('rememberMe')
        if rememberMe and rememberMe == 'on':
            request.session.set_expiry(1209600)
        user = authenticate(request, username=username, password=password)
        if not username or not password:
            messages.error(request, "Vui lòng nhập tên tài khoản và mật khẩu!")
            return HttpResponseRedirect('/')
        if user is not None:
            login(request, user)
            #if user.role == 'quanly':
            return redirect('quanly/')
            # elif user.role == 'nhanvien':
            #         return redirect('nhanvien')
            # elif user.role == 'kythuatvien':
            #         return redirect('kythuatvien')
        else:
            messages.error(request, "Tên đăng nhập hoặc mật khẩu không đúng. Vui lòng thử lại!")
            return HttpResponseRedirect('/')
        
def perform_logout(requet):
    return HttpResponseRedirect('/')
        
def render_trangchinh(request):
    listThietBi = ThietBi.objects.all()
    listPhong = Phong.objects.all()
    return render(request,"quanly.html",{'listThietBi': listThietBi, 'listPhong': listPhong})

def render_themthietbi(request):
    form = ThemThietBiForm()
    if request.method == "POST":
        form = ThemThietBiForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('QLthietbi_app:render_trangchinh')
    return render(request,"themtb.html", {'form': form}) 

def render_capnhap(request, pk):
    thietbi = get_object_or_404(ThietBi, pk=pk)
    form = ThemThietBiForm(instance=thietbi)
    if request.method == "POST":
        form = ThemThietBiForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('QLthietbi_app:render_trangchinh')
    return render(request,"themtb.html", {'form': form}) 

# AJAX
def load_phong(request):
    tang_id = request.GET.get('tang_id')
    listPhong = Phong.objects.filter(tang_id=tang_id).order_by('ten_phong')
    return render(request, 'phong_dropdown_list_options.html', {'listPhong': listPhong})

def render_chinhsuathietbi(request, id_thiet_bi):
    thietbi = ThietBi.objects.get(id_thiet_bi=id_thiet_bi)
    form = ThemThietBiForm(instance=thietbi)
    if request.method == "POST":
        form = ThemThietBiForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('QLthietbi_app:render_trangchinh')
    return render(request,"chinhsuatb.html", {'form': form})

def render_chitietthietbi(request, id_thiet_bi):
    thietbi = ThietBi.objects.get(id_thiet_bi=id_thiet_bi)
    return render(request,"chitiettb.html", {'thietbi': thietbi})
    
def render_xoathietbi(request, id_thiet_bi):
    thietbi = ThietBi.objects.get(id_thiet_bi=id_thiet_bi)
    thietbi.delete()
    return redirect('QLthietbi_app:render_trangchinh')

@csrf_exempt
def xoa_nhieuthietbi(request):
    if request.method == "POST":
        id_list = request.POST.getlist('instance')
        print(id_list)
        for id_thiet_bi in id_list:
            thietbi = ThietBi.objects.get(id_thiet_bi=id_thiet_bi)
            thietbi.delete()
        return redirect('QLthietbi_app:render_trangchinh')