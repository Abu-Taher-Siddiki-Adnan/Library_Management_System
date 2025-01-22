from django.db import models
from django.contrib.auth.models import User

GENRE_CHOICE = (
    ('Romance', 'Romance'),
    ('Fantasy', 'Fantasy'),
    ('Science Fiction', 'Science Fiction'),
    ('Paranormal', 'Paranormal'),
    ('Mystery', 'Mystery'),
    ('Horror', 'Horror'),
    ('Thriller', 'Thriller'),
    ('Action Adventure', 'Action Adventure'),
    ('Fiction', 'Fiction'),
)

class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(choices=GENRE_CHOICE, max_length=50, default="")
    publisher = models.CharField(max_length=100)
    publication_date = models.DateField(blank=True, null=True)
    available_copies = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.title

POSITION_CHOICE = (
    ('Librarians','Librarians'),
    ('Library Managers ','Library Managers'),
    ('Library Directors','Library Directors'),
)
class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=15)  
    email = models.EmailField(max_length=100)
    address = models.TextField(max_length=200)
    position = models.CharField(choices=POSITION_CHOICE,max_length=50)

    def __str__(self):
        return self.name