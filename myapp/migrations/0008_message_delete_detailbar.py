# Generated by Django 4.1.7 on 2023-08-25 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0007_contact_detailbar"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
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
                ("first", models.CharField(max_length=255)),
                ("first_en", models.CharField(max_length=255, null=True)),
                ("first_pl", models.CharField(max_length=255, null=True)),
                ("second", models.CharField(max_length=255)),
                ("second_en", models.CharField(max_length=255, null=True)),
                ("second_pl", models.CharField(max_length=255, null=True)),
                ("third", models.CharField(max_length=255)),
                ("third_en", models.CharField(max_length=255, null=True)),
                ("third_pl", models.CharField(max_length=255, null=True)),
                ("fourth", models.CharField(max_length=255)),
                ("fourth_en", models.CharField(max_length=255, null=True)),
                ("fourth_pl", models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name="DetailBar",
        ),
    ]
