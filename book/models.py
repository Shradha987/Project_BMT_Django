from django.db import models

# Create your models here.
class Books(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    book_title = models.CharField(max_length=100)
    # author = models.OneToOneField(book_title, null=True, blank=True)
    author = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    pub = models.CharField(max_length=100)
    pages = models.IntegerField()
    price = models.FloatField()
    cover_of_book = models.ImageField(upload_to='static/book/cover_photo/', null=True, blank=True)

    class Meta:
        db_table = 'Books_Master_1'