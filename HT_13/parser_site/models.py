from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=15, help_text='Represents url category name', blank=True)

    def __str__(self):
        return self.name


class Articles(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    id_article = models.IntegerField()
    title = models.TextField(default='title')
    text = models.TextField(default='text')
    time = models.IntegerField(default=0)
    descendants = models.CharField(max_length=70)
    by = models.CharField(max_length=70)
    kids = models.TextField(default='kids')
    type = models.CharField(max_length=70)
    score = models.TextField(default='score')
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.id_article, self.title, self.text, self.time, self.descendants, \
               self.by, self.kids, self.type, self.score, self.url, self.category_id
