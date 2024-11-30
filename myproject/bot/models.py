from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=225,verbose_name="Тауар атауы")
    description = models.TextField(verbose_name="Сипаттама")
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Бағасы")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Қосылған уақыты")

    def __str__(self):
        return self.name

    