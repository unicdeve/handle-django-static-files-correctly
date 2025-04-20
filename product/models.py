from django.db import models
from django.utils.translation import gettext_lazy as _
from category.models import Category
from django_assets.storage_backends import ProductImageStorage

class Product(models.Model):
    name = models.CharField(_('name'), max_length=200)
    description = models.TextField(_('description'), blank=True)
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name=_('category')
    )
    image = models.ImageField(_('image'), upload_to='products/', null=True, blank=True, storage=ProductImageStorage)
    is_available = models.BooleanField(_('is available'), default=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    @property
    def formatted_price(self):
        return f"${self.price:.2f}"
