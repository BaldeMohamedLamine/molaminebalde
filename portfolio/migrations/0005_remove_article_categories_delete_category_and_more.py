# Generated by Django 5.1.1 on 2024-09-23 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_category_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='categories',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
