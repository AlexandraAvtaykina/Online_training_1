# Generated by Django 4.2 on 2024-01-21 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_alter_user_ver_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ver_code',
            field=models.CharField(default='727238771248', max_length=15, verbose_name='Проверочный код'),
        ),
    ]
