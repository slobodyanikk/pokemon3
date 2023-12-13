from django.contrib import admin
from django.urls import path, include, re_path
from django.urls import path, include
from django.contrib.auth import views as auth_views

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('profile/', views.profile, name='profile'),
    re_path('', include('social_django.urls', namespace='social')),
    path('accounts/', include("django.contrib.auth.urls"), name='accounts'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('code-confirmation/', views.code_confirmation_view, name='code_confirmation'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
