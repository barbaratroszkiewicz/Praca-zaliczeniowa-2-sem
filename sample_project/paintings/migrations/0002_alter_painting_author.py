# Generated by Django 4.1.7 on 2023-04-18 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("authors", "0002_alter_author_country_of_origin"),
        ("paintings", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="painting",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="paintings",
                to="authors.author",
            ),
        ),
    ]