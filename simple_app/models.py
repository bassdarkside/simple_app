from django.db import models


class Currency(models.Model):
    code_a = models.CharField(max_length=3)
    code_b = models.CharField(max_length=3)
    date = models.IntegerField()
    sell = models.FloatField()
    buy = models.FloatField()
