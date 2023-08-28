# Generated by Django 4.1.7 on 2023-08-24 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0006_appbar_body_landing_remove_portell_data_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("title", models.CharField(max_length=255)),
                ("title_en", models.CharField(max_length=255, null=True)),
                ("title_pl", models.CharField(max_length=255, null=True)),
                ("description", models.TextField()),
                ("description_en", models.TextField(null=True)),
                ("description_pl", models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="DetailBar",
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
                ("title", models.CharField(max_length=255)),
            ],
        ),
    ]
