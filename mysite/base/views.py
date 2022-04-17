from django.shortcuts import render
from .models import User
from django.contrib.auth.hashers import check_password
import firebase_admin
from firebase_admin import credentials, auth


cred = credentials.Certificate("django-firebase-auth-cred.json")
admin = firebase_admin.initialize_app(cred)



# Create your views here.


def index(request):
    return render(request, 'base/index.html')
    
def signIn(request):
    return render(request,"base/login.html")
def home(request):
    return render(request,"base/home.html")
 
def postsignIn(request):
    email=request.POST.get('email')
    pasw=request.POST.get('pass')
    tenant = request.POST.get('tenant')
    try:
        # if there is no error then signin the user with given email and password
        # user=authe.sign_in_with_email_and_password(email,pasw)
        user = User.objects.get(email=email,tenant=tenant)
        matchcheck= check_password(pasw,user.password)
        custom_claims = {'id': user.id, 'tenant': user.tenant,'role':"ADMIN"}
        if matchcheck:
          token = auth.create_custom_token('b27e7408-be32-11ec-9d64-0242ac120002', custom_claims)
          print(token)

        
        
    except Exception as e:
      print(e)
      message="Invalid Credentials!!Please ChecK your Data"
      return render(request,"base/login.html",{"message":message})
    # session_id=user['idToken']
    # request.session['uid']=str(session_id)
    return render(request,"base/home.html",{"email":email})
 
def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,"base/login.html")
 
def signUp(request):
    return render(request,"base/registration.html")
 
def postsignUp(request):
     email = request.POST.get('email')
     passs = request.POST.get('pass')
     name = request.POST.get('name')
     try:
        # creating a user with the given email and password
        user=authe.create_user_with_email_and_password(email,passs)
        uid = user['localId']
        idtoken = request.session['uid']
        print(uid)
     except:
        return render(request, "base/registration.html")
     return render(request,"base/login.html")
