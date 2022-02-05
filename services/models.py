from django.db import models

# Create your models here.
class ServiceCategory(models.Model):
    service_category_name=models.CharField(max_length=30)

    def __str__(self):
        return self.service_category_name