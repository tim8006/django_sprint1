from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=256)

    def __str__(self):
        return self.title