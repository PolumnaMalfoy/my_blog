# Generated by Django 5.1.2 on 2024-10-12 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_delete_articles2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='published_time',
            field=models.DateTimeField(),
        ),
    ]
