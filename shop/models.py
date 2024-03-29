from django.db import models


class Publisher(models.Model):
    """出版社モデル"""
    class Meta:
        db_table = 'publisher'

    name = models.CharField(verbose_name='出版社名', max_length=255)

    def __str__(self):
        return self.name


class Author(models.Model):
    """著者モデル"""
    class Meta:
        db_table = 'author'

    name = models.CharField(verbose_name='著者名', max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """本モデル"""
    class Meta:
        db_table = 'book'

    title = models.CharField(verbose_name='タイトル', max_length=255)
    publisher = models.ForeignKey(Publisher, verbose_name='出版社',
                                      on_delete=models.PROTECT)
    authors = models.ManyToManyField(Author, verbose_name='著者')
    price = models.IntegerField(verbose_name='価格', null=True, blank=True)
    description = models.TextField(verbose_name='概要', null=True, blank=True)
    publish_date = models.DateField(verbose_name='出版日')

    def __str__(self):
        return self.title

