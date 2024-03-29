from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    date_of_release = models.DateTimeField()

    def __str__(self):
        return self.title
    
    class Meta:     
        permissions = (
                ("can_publish", "To publish a blog"),
                )