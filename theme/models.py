from django.db import models

class Location(models.Model):
    CHOICES = [
        ("KZ", "KAZARMU"),
        ("FD", "FIELD"),
        ("OUT", "OUTSIDE"),
    ]
    name = models.CharField(max_length=32,
    choices=CHOICES, default="KZ")
    date = models.DateField()

    def __str__(self):
        return f"{self.date.__str__()} -> {self.name}"


class Course(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    abr_name = models.CharField(max_length=16)
    full_name = models.CharField(max_length=64)

    def __str__(self):
        return self.abr_name