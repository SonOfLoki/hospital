from django.db import models
from django.urls import reverse

departments = (
    ('General Health', 'General Health'),
    ('Cardiology', 'Cardiology'),
    ('Dental', 'Dental'),
    ('Neurology', 'Neurology'),
    ('Orthopaedics', 'Orthopaedics')
)


class Appointment(models.Model):
    full_name = models.CharField(max_length=60)
    email = models.EmailField()
    date = models.DateField()
    department = models.CharField(choices=departments, max_length=50)
    number = models.BigIntegerField()
    message = models.TextField()

    def __str__(self):
        return self.full_name

class Doctor(models.Model):
    name = models.CharField(max_length=60)
    department = models.CharField(choices=departments, max_length=50)
    image = models.ImageField(default='default.jpg', upload_to='doctors')

    def __str__(self):
        return self.name

class News(models.Model):
    headline = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    date = models.DateField()
    image = models.ImageField(default='default.jpg', upload_to='news images')
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'News'
   
    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"slug": self.slug}) 
    

class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
