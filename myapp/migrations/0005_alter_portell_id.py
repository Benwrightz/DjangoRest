# Generated by Django 4.1.7 on 2023-07-19 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0004_alter_portell_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="portell",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
