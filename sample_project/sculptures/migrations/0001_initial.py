# Generated by Django 4.1.7 on 2023-04-18 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("authors", "0002_alter_author_country_of_origin"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sculpture",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(default="Unknown", max_length=150)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="sculptures",
                        to="authors.author",
                    ),
                ),
            ],
        ),
    ]