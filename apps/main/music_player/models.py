# Django
from django.db import models


class Music(models.Model):
    """
    This model is need for Admin panel.
    Admin can listen to music and do his works.
    """
    name = models.CharField(
        max_length=255
    )
    file = models.FileField()
    size_type = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    size = models.FloatField(
        blank=True,
        null=True
    )
    format_file = models.CharField(
        max_length=5
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        x = self.file.size
        y = 512000
        if x < y:
            self.size = round(x / 1000, 2)
            self.size_type = "kb"
        elif x < y * 1000:
            self.size = round(x / 1000000, 2)
            self.size_type = "mb"
        else:
            self.size = round(x / 1000000000, 2)
            self.size_type = "gb"

        self.format_file = str(self.file).split(".")[-1].upper()
        super(Music, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Music'
        verbose_name_plural = 'Musics'
