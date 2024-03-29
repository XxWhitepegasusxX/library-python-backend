from django.db import models
from uuid import uuid4
# Create your models here.

def upload_to(instance, filename):
    # Função para determinar o caminho de upload com base no tipo de arquivo
    if isinstance(instance, Book):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            return 'images/' + filename
        elif filename.endswith('.pdf') or filename.endswith('.doc'):
            return 'documents/' + filename
    return filename


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=150)
    release_year = models.IntegerField()
    pages = models.IntegerField()
    added_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    document = models.FileField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.title
    
class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=150)
    books = models.ManyToManyField(Book, related_name="author", blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=150)
    books = models.ManyToManyField(Book, related_name="category", blank=True)

    def __str__(self):
        return self.name