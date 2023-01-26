# Generated by Django 4.1.3 on 2023-01-26 14:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Data",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("type", models.IntegerField()),
                ("date_and_hour", models.DateTimeField()),
                ("value", models.FloatField()),
                ("cpf", models.CharField(max_length=11)),
                ("credit_card", models.CharField(max_length=12)),
                ("owner", models.CharField(max_length=50)),
                ("company_name", models.CharField(max_length=50)),
            ],
        ),
    ]
