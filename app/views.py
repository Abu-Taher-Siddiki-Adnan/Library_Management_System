from django.shortcuts import render,get_object_or_404, redirect
from .models import Books,Employee
from .forms import BookForm,RegistrationForm,LoginForm,ProfileForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.db.models import Q

def home(request):
    return render(request, 'app/home.html')

def book_list(request):
    books = Books.objects.all()
    return render(request, 'app/book_list.html', {'books': books})

def update_book_copies(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Books, id=book_id)
        available_copies = request.POST.get('available_copies')

        if available_copies.isdigit():
            book.available_copies = int(available_copies)
            book.save()

    return redirect('book_list') 

def add(request):
  if request.method == 'POST':
    form = BookForm(request.POST)
    if form.is_valid():
      new_title = form.cleaned_data['title']
      new_author = form.cleaned_data['author']
      new_genre = form.cleaned_data['genre']
      new_publisher = form.cleaned_data['publisher']
      new_publication_date = form.cleaned_data['publication_date']
      new_available_copies = form.cleaned_data['available_copies']

      new_book = Books(
        title=new_title,
        author=new_author,
        genre=new_genre,
        publisher=new_publisher,
        publication_date=new_publication_date,
        available_copies=new_available_copies
      )
      new_book.save()
      return render(request, 'app/add.html', {
        'form': BookForm(),
        'success': True
      })
  else:
    form = BookForm()
  return render(request, 'app/add.html', {
    'form': BookForm()
  })

def delete(request, id):
  if request.method == 'POST':
    book = Books.objects.get(pk=id)
    book.delete()
  return HttpResponseRedirect(reverse('book_list'))


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'app/registration.html', context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User registration was successful.")
            return redirect('login')  
        else:
            messages.warning(request, "Invalid input data. Please correct the errors below.")

        context = {'form': form}
        return render(request, 'app/registration.html', context)

class EmployeeLoginView(LoginView):
    template_name = 'app/login.html' 
    authentication_form = LoginForm 

class ProfileView(View):
    def get(self, request):
        form = ProfileForm()
        profile = Employee.objects.filter(user=request.user).last()
        return render(request, 'app/profile.html', {'form': form, 'profile': profile})
    
    def post(self, request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            position = form.cleaned_data['position']
            reg = Employee(user=user, name=name, mobile=mobile, email=email, address=address, position=position)
            reg.save()
            messages.success(request, "Congratulations! Profile Saved Successfully")
        else:
            messages.warning(request, "Invalid data Input")
        profile = Employee.objects.filter(user=request.user).last()
        return render(request, 'app/profile.html', {'form': form, 'profile': profile})


def update_profile(request, id):
    profile = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'app/update_profile.html', {'form': form, 'profile': profile})


def search(request):
    try:
        query = request.GET.get('q', '').strip()
        books = Books.objects.all()

        if query:
            books = books.filter(title__icontains=query)
            
        return render(request, 'app/search.html', {'books': books, 'query': query})
    
    except Exception as e:
        return render(request, 'app/search.html', {'error': str(e)})

