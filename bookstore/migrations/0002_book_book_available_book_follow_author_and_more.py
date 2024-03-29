# Generated by Django 5.0.2 on 2024-03-05 15:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bookstore", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="book_available",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="book",
            name="follow_author",
            field=models.CharField(blank=True, max_length=2083),
        ),
        migrations.AddField(
            model_name="book",
            name="image_url",
            field=models.CharField(default=False, max_length=2083),
        ),
    ]
