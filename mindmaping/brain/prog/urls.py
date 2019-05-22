from django.urls import path
from django.contrib import admin
from django.conf.urls import url,include
from brain.prog import views

# from . import views


urlpatterns = [
   path(r'^$', include('prog.urls.py')),
   url(r'^$',views.individual_post),
   path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^brain/',include('brain.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),

]



