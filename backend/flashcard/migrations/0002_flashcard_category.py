# Generated by Django 3.1.3 on 2020-11-17 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flashcard',
            name='category',
            field=models.CharField(default='', max_length=120),
        ),
    ]