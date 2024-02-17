from django.db import models

# Create your models here.

class Plato(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.TextField(null=False)

    class Meta:
        db_table = 'platos'