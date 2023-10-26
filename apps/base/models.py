from django.db import models

class Application(models.Model):
    user = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self) -> str:
        return self.user