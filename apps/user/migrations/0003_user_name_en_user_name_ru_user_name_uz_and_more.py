# Generated by Django 4.1.7 on 2023-03-18 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='name_ru',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='name_uz',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='surname_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='surname_ru',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='surname_uz',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
