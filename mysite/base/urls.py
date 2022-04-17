from django.urls import path
from . import views

urlpatterns = [
  # path('', views.index, name='index'),
  path('', views.signIn),
  path('postsignIn/', views.postsignIn),
  path('signUp/', views.signUp, name="signup"),
  path('logout/', views.logout, name="log"),
  path('postsignUp/', views.postsignUp),
]