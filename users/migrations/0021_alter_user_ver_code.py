# Generated by Django 4.2 on 2024-01-21 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_alter_user_ver_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ver_code',
            field=models.CharField(default='264571675377', max_length=15, verbose_name='Проверочный код'),
        ),
    ]
