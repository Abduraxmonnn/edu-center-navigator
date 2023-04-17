# Generated by Django 4.1.7 on 2023-03-18 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='description_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='name_uz',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
