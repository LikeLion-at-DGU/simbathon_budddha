# Generated by Django 4.2.1 on 2023-06-24 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qnapage', '0010_remove_qnacomment_parent_comment_qnareply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qna',
            name='pub_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='qnacomment',
            name='pub_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='qnareply',
            name='pub_date',
            field=models.DateTimeField(),
        ),
    ]
