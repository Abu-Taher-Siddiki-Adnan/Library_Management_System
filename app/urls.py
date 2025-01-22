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
    path('search/', views.search, name='search'),

    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
]
