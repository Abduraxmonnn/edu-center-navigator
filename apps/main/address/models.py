# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
    """
    This model used to save Addresses of any Center or Branches of Centers.
    """

    # noinspection SpellCheckingInspection
    class Districts(models.TextChoices):
        MIRZO_ULUGBEK = 'MIRZO_ULUGBEK', _('MIRZO ULUG\'BEK')
        SHAYXONTOXUR = 'SHAYXONTOXUR', _('SHAYXONTOXUR')
        YANGIHAYOT = 'YANGIHAYOT', _('YANGIHAYOT')
        YAKKASARAY = 'YAKKASARAY', _('YAKKASARAY')
        YUNUSOBOD = 'YUNUSOBOD', _('YUNUSOBOD')
        CHILANZAR = 'CHILANZAR', _('CHILANZAR')
        YASHNOBOD = 'YASHNOBOD', _('YASHNOBOD')
        BEKTEMIR = 'BEKTEMIR', _('BEKTEMIR')
        MIROBOD = 'MIROBOD', _('MIROBOD')
        SERGELI = 'SERGELI', _('SERGELI')
        OLMAZOR = 'OLMAZOR', _('OLMAZOR')
        UCHTEPA = 'UCHTEPA', _('UCHTEPA')

    district = models.CharField(
        max_length=13,
        choices=Districts.choices,
        default=Districts.YUNUSOBOD
    )
    street = models.CharField(
        max_length=255
    )
    apartment_letter = models.CharField(
        max_length=3,
        blank=True,
        null=True
    )
    apartment_number = models.IntegerField()
    lat = models.DecimalField(
        max_digits=9,
        decimal_places=6
    )
    lng = models.DecimalField(
        max_digits=9,
        decimal_places=6
    )
    created_date = models.DateField(
        auto_now_add=True
    )
    last_updated = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.district} - {self.street} - ' \
               f'{self.apartment_letter}{self.apartment_number} - {self.lat} - {self.lng}'

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
