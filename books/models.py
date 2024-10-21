from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, default='3421231242')
    pages = models.IntegerField(null=False, default=0)
    language = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title
