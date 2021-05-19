from django.db import models

# Create your models here.


class Cotizacion(models.Model):
    compra_billetes = models.DecimalField(max_digits=7, decimal_places=4)
    venta_billetes = models.DecimalField(max_digits=7, decimal_places=4)
    compra_divisas = models.DecimalField(max_digits=7, decimal_places=4)
    venta_divisas = models.DecimalField(max_digits=7, decimal_places=4)

    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return u"%s" % self.id