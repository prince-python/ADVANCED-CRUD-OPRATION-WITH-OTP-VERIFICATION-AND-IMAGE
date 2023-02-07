from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
urlpatterns = [
    path('',views.index),
    path('login',views.login,name='login'),
    path("verifyotp",views.verifyotp,name="verifyotp"),
    path('delete/<int:id>',views.delete,name='delete'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
