from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import userPasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from registration.models import Advisor
from django.http import HttpResponse

# when the user to log in
# corresponding teamp: login.html
# for GET: render login.html with Django AuthenticationForm
# for POST: 
#   call Django authenticate function
#   after authentcation, check whether the user is an Advisor using user
#   redirect to home.html
def loginAccount(request):

    if request.method == 'GET':
        return render(request, 'login.html', {'form':AuthenticationForm})
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password']
                           )
        if user is None:
            return render(request,'login.html',
                                  {'form': AuthenticationForm(),
                                   'error': 'username and password do not match'
                                  }
                         )
        else:
            login(request,user)
    try:
         advisor = Advisor.objects.get(user=request.user)
         return render(request, 'home.html', {'advisor':advisor})
    except Advisor.DoesNotExist:
         return render(request, 'home.html') 

@login_required
def logoutAccount(request):        
    logout(request)
    return redirect('home')

# for logged in user, allow to change password
# corresponding template: change_password.html
# for GET: render change_password.html with userPassordChangeForm
# for POST
#   check new password matches confirmation new password
#   check the userPasswordChangeForm
#   update user password
#   if any errors, render change_password.html 
#   if success, redirect to password_changed.html
@login_required
def changePassword(request):
    if request.method == 'POST':
        if request.POST['new_password1'] == request.POST['new_password2']:
            form = userPasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                return redirect('pwdChanged')
            else:
                return render(request, 'change_password.html', 
                                       {'form':userPasswordChangeForm(request.user), 
                                        'error':form.errors}
                             )

        else: 
            return render(request, 'change_password.html', 
                                    {'form':userPasswordChangeForm(request.user),
                                     'error':'Passwords do not match'}
                         )
    else:
        form = userPasswordChangeForm(request.user)
        try:
            advisor = Advisor.objects.get(user=request.user)
            return render(request, 'change_password.html', {'form':form, 'advisor':advisor})
        except Advisor.DoesNotExist: 
            return render(request, 'change_password.html', {'form':form}) 

def passwordChanged(request):
    try:
        advisor = Advisor.objects.get(user=request.user)
        return render(request, 'password_changed.html', {'advisor':advisor})
    except Advisor.DoesNotExist: 
        return render(request, 'password_changed.html')
