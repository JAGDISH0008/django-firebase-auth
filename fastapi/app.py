from typing import Optional

from fastapi import FastAPI, Header
import firebase_admin
from firebase_admin import credentials, auth

app = FastAPI()

cred = credentials.Certificate("django-firebase-auth-cred.json")
admin = firebase_admin.initialize_app(cred)

@app.get("/")
def read_root(x_auth_token: Optional[str] = Header(None)):
  decoded_token = auth.verify_id_token(x_auth_token)
  print("++++++++++++++++")
  print(decoded_token)
  print("+++++++++++++++++")
  return {"Hello": "World"}

