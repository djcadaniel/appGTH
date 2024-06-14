from django.db import models

# Create your models here.
class Contratos(models.Model):
  name = models.CharField(max_length=50, blank=False, null=False)
  dni = models.CharField(max_length=8, blank=True, null=True)

  def __str__(self):
    return self.name