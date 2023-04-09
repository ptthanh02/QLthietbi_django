from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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
            return redirect('Trangchinh/')
            # elif user.role == 'nhanvien':
            #         return redirect('nhanvien')
            # elif user.role == 'kythuatvien':
            #         return redirect('kythuatvien')
        else:
            messages.error(request, "Tên đăng nhập hoặc mật khẩu không đúng. Vui lòng thử lại!")
            return HttpResponseRedirect('/')
        
def render_trangchinh(request):
    return render(request, 'quanly.html')

def perform_logout(requet):
    return HttpResponseRedirect('/')