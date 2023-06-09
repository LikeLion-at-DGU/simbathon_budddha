# Generated by Django 4.2 on 2023-06-19 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("mainpage", "0003_alter_ticket_nickname_alter_ticket_pub_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="nickname",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
