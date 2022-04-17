import firebase_admin
from firebase_admin import credentials, auth


cred = credentials.Certificate("django-firebase-auth-cred.json")
admin = firebase_admin.initialize_app(cred)
custom_claims = {'id': "1", 'tenant': "test1",'role':"ADMIN"}
token = auth.sign_in_with_email_and_password("jagadeesh26597@gmail.com","test@123")
print(token)
