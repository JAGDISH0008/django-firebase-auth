from django.shortcuts import render
from .models import User
from django.contrib.auth.hashers import check_password
import os
from .config.firebase import firebaseConfig
import firebase_admin
from firebase_admin import credentials, auth
import pyrebase


cred = credentials.Certificate("django-firebase-auth-cred.json")
admin = firebase_admin.initialize_app(cred)

# config={
#     'apiKey': os.environ['API_KEY'],
#     'authDomain':os.environ['AUTH_DOMAIN'],
#     'projectId':  os.environ['PROJECT_ID'],
#     'storageBucket': os.environ['STORAGE_BUCKET'],
#     'messagingSenderId':  os.environ['MESSAGING_SENDER_ID'],
#     'appId': os.environ['APP_ID'],
# }

firebase=pyrebase.initialize_app(firebaseConfig)
authe = firebase.auth()

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
        user=authe.sign_in_with_email_and_password(email,pasw)
        print("++++++++++++++++")
        print(user)
        print("+++++++++++++++++")
        if user:
            user_details = User.objects.get(firebaseid=user['localId'],tenant=tenant)
            custom_claims = {'id': user['localId'], 'tenant': user_details.tenant,'role':"ADMIN"}
            auth.set_custom_user_claims(user['localId'],custom_claims)
            print("++++++++++++++++")
            print(user)
            print("+++++++++++++++++")
            
        # print("++++++++++++++++")
        # print(user)
        # print("+++++++++++++++++")
        
        
       
        # if matchcheck:
        #   token = auth.create_custom_token('b27e7408-be32-11ec-9d64-0242ac120002', custom_claims)
        #   result = auth.sign_in_with_custom_token(token)
        #   print("++++++++++++++")
        #   print(token)
        #   print("++++++++++++++")
        #   print(result)
        #   print("++++++++++++++")
          

        
        
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
     tenant = request.POST.get('tenant')
     try:
        # creating a user with the given email and password
        user=authe.create_user_with_email_and_password(email,passs)
        uid = user['localId']
        if user:
            User.objects.create(email=email,tenant=tenant,name=name,firebaseid=uid)
        # idtoken = request.session['uid']
        print(uid)
     except Exception as e:
        print(e)
        return render(request, "base/registration.html")
     return render(request,"base/login.html")
