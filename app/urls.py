from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('add/', views.add, name='add'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update-book-copies/<int:book_id>/', views.update_book_copies, name='update_book_copies'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('update_profile/<int:id>/', views.update_profile, name='update_profile'),
    path('search/', views.search_books, name='search_books'),

    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/password_change.html'), name='passwordchange'),
    path('passwordchange/done/', auth_views.PasswordChangeDoneView.as_view(template_name='app/password_change_done.html'), name='password_change_done'),
    
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
]
