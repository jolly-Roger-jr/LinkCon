# Generated by Django 4.1.1 on 2022-10-07 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=249, verbose_name='Исходная ссылка')),
            ],
            options={
                'verbose_name': 'Исходная ссылка',
                'verbose_name_plural': 'Исходные ссылки',
            },
        ),
        migrations.DeleteModel(
            name='Link',
        ),
    ]
