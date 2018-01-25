from django.db import models


class Project(models.Model):
    photo = models.BinaryField()
    name = models.CharField(max_length=200)
    blurb = models.CharField(max_length=200)
    goal = models.CharField(max_length=200)
    pledged = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    usd_pledged = models.FloatField()


class Askstories(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(default='title')
    text = models.TextField(default='text')
    time = models.IntegerField(default=0)
    descendants = models.CharField(max_length=70)
    by = models.CharField(max_length=70)
    kids = models.TextField(default='kids')
    type = models.CharField(max_length=70)
    score = models.IntegerField(default=0)
    url = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id, self.title, self.text, self.time,
                   self.descendants, self.by, self.kids, self.type, self.score, self.url)


class Showstories(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(default='title')
    text = models.TextField(default='text')
    time = models.IntegerField(default=0)
    descendants = models.CharField(max_length=70)
    by = models.CharField(max_length=70)
    kids = models.TextField(default='kids')
    type = models.CharField(max_length=70)
    score = models.IntegerField(default=0)
    url = models.CharField(max_length=200)


class Newstories(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(default='title')
    text = models.TextField(default='text')
    time = models.IntegerField(default=0)
    descendants = models.CharField(max_length=70)
    by = models.CharField(max_length=70)
    kids = models.TextField(default='kids')
    type = models.CharField(max_length=70)
    score = models.IntegerField(default=0)
    url = models.CharField(max_length=200)


class Jobstories(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(default='title')
    text = models.TextField(default='text')
    time = models.IntegerField(default=0)
    descendants = models.CharField(max_length=70)
    by = models.CharField(max_length=70)
    kids = models.TextField(default='kids')
    type = models.CharField(max_length=70)
    score = models.IntegerField(default=0)
    url = models.CharField(max_length=200)
