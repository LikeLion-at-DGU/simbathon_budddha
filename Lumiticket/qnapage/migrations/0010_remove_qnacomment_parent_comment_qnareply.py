# Generated by Django 4.2.1 on 2023-06-24 03:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qnapage', '0009_alter_qna_pub_date_alter_qnacomment_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qnacomment',
            name='parent_comment',
        ),
        migrations.CreateModel(
            name='QnaReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('pub_date', models.DateField()),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qnapage.qnacomment')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
