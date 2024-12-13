from django.urls import re_path
from PetSitterApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns= [
    re_path(r'^availability$',views.availabilityApi),
    re_path(r'^availability/(\d+)$',views.availabilityApi),

    re_path(r'^role$', views.roleApi),
    re_path(r'^role/(\d+)$', views.roleApi),

    re_path(r'^reservation$', views.reservationApi),
    re_path(r'^reservation/(\d+)$', views.reservationApi),

    re_path(r'^pet$', views.petApi),
    re_path(r'^pet/(\d+)$', views.petApi),

    re_path(r'^user$', views.userApi),
    re_path(r'^user/(\d+)$', views.userApi),
    re_path('register/', views.register, name='register'),
    re_path('login/', views.login, name='login'),

    re_path(r'^service$', views.serviceApi),
    re_path(r'^service/(\d+)$', views.serviceApi),
    
    re_path(r'^sitter$', views.sitterApi),
    re_path(r'^sitter/(\d+)$', views.sitterApi),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




