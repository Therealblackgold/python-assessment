from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Homepage
    path('', views.homepage, name="homepage"),
    # Register
    path('register', views.registerUser, name="register"),
    # Login
    path('login', views.loginUser, name="login"),
    # Logout
    path('logout', views.logoutUser, name="logout"),
    # Update User
    path('update-user/<int:user_id>', views.updateUser, name="update-user"),

    ### -----------------PASSWORD RESET-------------------- ####
    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name="accounts/password_reset.html"),
         name="reset_password"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name="accounts/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="accounts/password_reset_form.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="accounts/password_reset_done.html"),
         name="password_reset_complete"),
]
