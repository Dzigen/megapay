from django.db import models

# Create your models here.

class test(models.Model):

    text_d = models.CharField(max_length=100)

    class Meta:
        db_table = "test"