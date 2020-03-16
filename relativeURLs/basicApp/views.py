from django.shortcuts import render
from basicApp.forms import UserForm, UserProfileInfoForm
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth import login,authenticate,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required



context_dict={'text': 'hello world!','number':100}

# Create your views here.
def index(request):
    return render(request, 'basicApp/index.html',context_dict)

@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return render(request, 'basicApp/other.html')

def registration(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()

    return render(request, 'basicApp/registration.html',
                                    {'user_form':user_form,
                                    'profile_form':profile_form,
                                    'registered':registered})


def userLogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account Not Active")

        else:
            print("Someone tried to login and failed")
            print("Username: {} and  Password: {}".format(username,password))
            return HttpResponse("Invalid Login Details Supplied")

    else:
        return render(request,'basicApp/login.html',{})
