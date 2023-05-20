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
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
import csv
import io
from .filters import ThietBiFilter


def tao_file_txt(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="thietbi.txt"'
    listThietBi = ThietBi.objects.all()
    lines = []
    for thietbi in listThietBi:
        ngay_mua = thietbi.ngay_mua.strftime('%d/%m/%Y') if thietbi.ngay_mua else ''
        ngay_bao_tri = thietbi.ngay_bao_tri.strftime('%d/%m/%Y') if thietbi.ngay_bao_tri else ''
        lines.append(f'Tên thiết bị: {thietbi.ten_thiet_bi}\n'
                     f'Loại thiết bị: {thietbi.loai_thiet_bi.ten_loaithietbi}\n'
                     f'Phòng: {thietbi.phong.ten_phong}\n'
                     f'Tầng: {thietbi.tang.ten_tang}\n'
                     f'Ngày mua: {ngay_mua}\n'
                     f'Giá mua: {thietbi.gia_mua}\n'
                     f'Tình trạng: {thietbi.tinh_trang}\n'
                     f'Ngày bảo trì: {ngay_bao_tri}\n'
                     f'Mô tả: {thietbi.mo_ta}\n\n')
    response.writelines(lines)
    return response

def tao_file_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="thietbi.csv"'

    listThietBi = ThietBi.objects.all()

    csv_buffer = io.StringIO()
    writer = csv.writer(csv_buffer)
    writer.writerow(['Tên thiết bị', 'Loại thiết bị', 'Phòng', 'Tầng', 'Ngày mua', 'Giá mua', 'Tình trạng', 'Ngày bảo trì', 'Mô tả'])

    for thietbi in listThietBi:
        ngay_mua = thietbi.ngay_mua.strftime('%d/%m/%Y') if thietbi.ngay_mua else ''
        ngay_bao_tri = thietbi.ngay_bao_tri.strftime('%d/%m/%Y') if thietbi.ngay_bao_tri else ''
        writer.writerow([
            thietbi.ten_thiet_bi,
            thietbi.loai_thiet_bi.ten_loaithietbi,
            thietbi.phong.ten_phong,
            thietbi.tang.ten_tang,
            ngay_mua,
            thietbi.gia_mua,
            thietbi.tinh_trang,
            ngay_bao_tri,
            thietbi.mo_ta
        ])

    csv_buffer.seek(0)
    response.write(csv_buffer.getvalue().encode('utf-8-sig'))

    return response

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
        
# def render_trangchinh(request):
#     listThietBi = ThietBi.objects.all()
#     return render(request,"quanly.html",{'listThietBi': listThietBi})

class ThietBi_view(View):
    def get(self, request):
        listThietBi = ThietBi.objects.all()
        thietbi_count = listThietBi.count()
        myFilter = ThietBiFilter(request.GET, queryset=listThietBi)
        listThietBi = myFilter.qs
        return render(request,"quanly.html",{'listThietBi': listThietBi, 'myFilter': myFilter})
    
    def post(self, request):
        if request.method == "POST":
            selected_rows = request.POST.getlist('selectedItems[]')
            for id in selected_rows:
                thietbi = ThietBi.objects.get(pk=id)
                thietbi.delete()
        return redirect('QLthietbi_app:render_trangchinh')

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
        form = ThemThietBiForm(request.POST,request.FILES,instance=thietbi)
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
def render_xoanhieutthietbi(request):
    if request.method == "POST":
        selected_rows = request.POST.getlist('list')
        for id in selected_rows:
            thietbi = ThietBi.objects.get(id_thiet_bi=id)
            thietbi.delete()
    return redirect('QLthietbi_app:render_trangchinh')

