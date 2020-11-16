from django.urls import path
from .views import registro, login
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from .forms import loginForm

urlpatterns = [
    path('registro/',registro,name = "registro"),
    path('',login,name = "login"),
    path('logout/',LogoutView.as_view(template_name='login.html'),name = "logout"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)