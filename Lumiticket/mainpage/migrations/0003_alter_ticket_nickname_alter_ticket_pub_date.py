# Generated by Django 4.2 on 2023-06-19 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainpage", "0002_alter_ticket_nickname_alter_ticket_pub_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="nickname",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="pub_date",
            field=models.DateTimeField(),
        ),
    ]
