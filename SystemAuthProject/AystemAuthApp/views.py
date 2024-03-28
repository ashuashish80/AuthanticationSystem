from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm,PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from AystemAuthApp import forms
from django.contrib import messages
# Create your views here.

def user_signup(request):
    if request.method=='POST':
        fm = forms.signupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.info(request,'signup sucessfully done please login')
            return redirect('/login')
    else:
        fm = forms.signupForm()
    return render(request,'signup.html',{'form':fm})

def user_login(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request= request, data= request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            print(uname)
            passw = fm.cleaned_data['password']
            print(passw)
            user = authenticate(username=uname,password=passw)
            if user is not None:
                login(request, user)
                messages.info(request,f'login sucessfully welcome {request.user}')
                return redirect('/profile')
            else:
                messages.info(request,"please enter valid details.....")
    else:
        fm = AuthenticationForm()
    return render(request,'login.html',{'form':fm})

def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = forms.profileform(request.POST, instance = request.user)
            if fm.is_valid():
                fm.save()
                messages.info(request,'data updated sucessfully...')
        else:
            fm = forms.profileform(instance = request.user)
        return render(request,'profile.html',{'name':request.user, 'form':fm})
    else:
        messages.info(request,'please enter valod details...')
        return redirect('/login')
    
def user_logout(request):
    if request.user.is_authenticated:
        name1 = request.user
        logout(request)
        messages.info(request,f'logout sucessfully..{name1}')
        return redirect('/login')
    else:
        messages.info(request,'invalid request')

# PasswordChangeForm
def passwordchange(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data=request.data)
            if fm.is_valid():
                update_session_auth_hash(request,request.user)
                name1 = request.user
                fm.save()
                messages.info(request,f"your password is sucessfully changed for {name1} please relogin....")
                return redirect('logout')
        else:
            fm = PasswordChangeForm(user=request.user)
    else:
        messages.info(request,'please login to change password')
        return redirect('/login')
    return render(request,'passwordchange.html',{'form':fm})


#set password

def setpassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                update_session_auth_hash(request,request.user)
                fm.save()
                messages.info(request,'password set sucessfully please relogin with new password')
                return redirect("/logout")
        else:
            fm = SetPasswordForm(user=request.user)

    else:
        messages.info(request,"invalid request")
        return redirect("/login")
    return render(request,'setpass.html',{"form":fm})