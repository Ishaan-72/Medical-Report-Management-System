from django.urls import path

from . import views

app_name='accounts'

urlpatterns = [
    path('',views.home,name='accounts'),
    path('deletereport',views.deletereport,name='deletereport'),
    path('signup',views.handlesignup,name='signup'),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('reports/',views.reports,name='home'),
    path('postreport',views.postreport,name="postreport"),
    path('user_reports',views.userreport,name="userreport"),
    path('about',views.about,name="about"),
]