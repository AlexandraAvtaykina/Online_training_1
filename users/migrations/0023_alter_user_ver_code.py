# Generated by Django 4.2 on 2024-01-21 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_alter_user_ver_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ver_code',
            field=models.CharField(default='662843390262', max_length=15, verbose_name='Проверочный код'),
        ),
    ]
