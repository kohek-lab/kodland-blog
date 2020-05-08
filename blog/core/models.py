from django.db import models


class Post(models.Model):
    post_title = models.CharField(max_length=500)
    post_body = models.TextField()
    post_image = models.ImageField(upload_to='images/posts-images/')
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creation_date']

    def __str__(self):
        return self.post_title
