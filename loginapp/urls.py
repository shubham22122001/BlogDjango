from django.urls import path
# from login import settings
from . import views
# from django.conf.urls.static import static 
urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('doctor/', views.doctor, name='doctor'),
    path('patient/', views.patient, name='patient'),
    path('', views.logout, name='logout_view'),
    path('blogdetails', views.blogdetails, name='blogdetails'),
    path('blog', views.blog, name='blog'),
    path('patient_blog', views.patient_blog, name='patient_blog'),




] 
# + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)