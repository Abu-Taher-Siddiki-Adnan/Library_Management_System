# Generated by Django 5.1.4 on 2025-01-20 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='genre',
            field=models.CharField(choices=[('Romance', 'Romance'), ('Fantasy', 'Fantasy'), ('Science Fiction', 'Science Fiction'), ('Paranormal', 'Paranormal'), ('Mystery', 'Mystery'), ('Horror', 'Horror'), ('Thriller', 'Thriller'), ('Action Adventure', 'Action Adventure'), ('Fiction', 'Fiction')], default='Fiction', max_length=50),
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]
