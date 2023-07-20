from django.core.exceptions import ValidationError
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    venue = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_fee = models.BooleanField(default=True)

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError("Start date can't be greater than End date")

    def __str__(self):
        return self.title
