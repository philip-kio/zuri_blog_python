from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length= 200 )
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    body = models.TextField()

    @property
    def number_of_comments(self):
        return Comment.objects.filter(post=self).count()
    


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])




class Comment(models.Model):
    posts = models.ForeignKey(post, on_delete= models.CASCADE, related_name = 'comments',)
    comment = models.CharField(max_length=240)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,)
    date_posted = models.DateTimeField(default=timezone.now)    

    def __str__(self):
        return self.comment


    def get_absolute_url(self):
        return reverse('', args=[str(self.pk)])