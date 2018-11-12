from django.urls import path

from . import views

urlpatterns = [
	path('signup/', views.SignUp.as_view(), name='signup'),
	path('', views.simple_upload, name='simple_upload'),
	path('', views.model_form_upload, name='model_form_upload'),
]