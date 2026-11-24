from django.db import models


class Student(models.Model):
    first_name = models.CharField("prénom", max_length=100)
    last_name = models.CharField("nom", max_length=100)
    email = models.EmailField(unique=True)
    classe = models.CharField(max_length=10)
    phone = models.CharField("téléphone", max_length=20, blank=True)
    birth_date = models.DateField("date de naissance", null=True, blank=True)
    active = models.BooleanField("actif", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
