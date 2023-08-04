from django.db import models

# Create your models here.
class Post(models.Model):
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank = True, null = True)
    tags = models.ManyToManyField('Tag', blank=True)
    title = models.CharField('Title', max_length=50)
    descrption = models.CharField('Description', max_length=100, blank=True, help_text='simple one-line text')
    image = models.ImageField('Image', upload_to='blog/%Y/%m/', blank=True, null=True)
    content = models.TextField('Content')
    created_dt = models.DateTimeField('Created dt', auto_now_add=True)
    update_dt = models.DateTimeField('Update dt', auto_now=True)
    like = models.PositiveSmallIntegerField('Like', default=0)

    class Meta:
        ordering = ['update_dt']

    def __str__ (self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField('Description', max_length=100, blank=True, help_text='simple one-line text')

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

class Comment(models.Model):
    pass
