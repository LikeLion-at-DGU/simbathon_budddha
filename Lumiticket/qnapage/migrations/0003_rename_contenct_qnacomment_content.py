# Generated by Django 4.2.1 on 2023-06-22 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qnapage', '0002_qnacomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qnacomment',
            old_name='contenct',
            new_name='content',
        ),
    ]
