# Generated by Django 4.1.1 on 2022-10-13 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_link_shortlink_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='shortlink_url',
            field=models.CharField(max_length=6, verbose_name='Сокращенная ссылка'),
        ),
    ]
