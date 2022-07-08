# Generated by Django 3.2.13 on 2022-07-08 09:00

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Card",
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
                ("recipient", models.CharField(max_length=50, null=True)),
                ("content", models.TextField()),
                ("token", models.UUIDField(default=uuid.uuid4, unique=True)),
                ("count", models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
