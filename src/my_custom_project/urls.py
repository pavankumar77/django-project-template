from django.conf.urls import patterns, include, url
from todoapp import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin 
admin.autodiscover()

urlpatterns = patterns('',

   
   # url(r'^logout/', views.logout),
   # url(r'^auth/', views.auth_view,),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', views.sign_in),
    url(r'^registration/', views.registration),  
    url(r'^tasks/$', views.tasks,), 
    url(r'^tasks/filter/', views.fiter_by_accessibility,),   
    url(r'^create_tasks/', views.create_task),
    url(r'^user/', views.user),
    
    
   )
