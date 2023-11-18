from django.db import models

class Portfolio(models.Model):
    about = models.TextField(blank=True)
    image = models.ImageField(null=True,blank=False)
    text = models.TextField(blank=False)

    def __str__(self) -> str:
        return self.text
