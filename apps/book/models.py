from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='тема')
    author = models.CharField(max_length=255, null=False, blank=False, verbose_name='автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создание')
    pages = models.PositiveIntegerField(null=False, blank=False, verbose_name='страница')
    logo = models.ImageField(upload_to='book_covers/', null=True, blank=True, verbose_name='логотип')

    def __str__(self):
        return self.title
