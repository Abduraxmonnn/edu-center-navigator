# Generated by Django 4.1.7 on 2023-03-13 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(choices=[('MIRZO_ULUGBEK', "MIRZO ULUG'BEK"), ('SHAYXONTOXUR', 'SHAYXONTOXUR'), ('YANGIHAYOT', 'YANGIHAYOT'), ('YAKKASARAY', 'YAKKASARAY'), ('YUNUSOBOD', 'YUNUSOBOD'), ('CHILANZAR', 'CHILANZAR'), ('YASHNOBOD', 'YASHNOBOD'), ('BEKTEMIR', 'BEKTEMIR'), ('MIROBOD', 'MIROBOD'), ('SERGELI', 'SERGELI'), ('OLMAZOR', 'OLMAZOR'), ('UCHTEPA', 'UCHTEPA')], default='YUNUSOBOD', max_length=13)),
                ('street', models.CharField(max_length=255)),
                ('apartment_letter', models.CharField(blank=True, max_length=3, null=True)),
                ('apartment_number', models.IntegerField()),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lng', models.DecimalField(decimal_places=6, max_digits=9)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]
