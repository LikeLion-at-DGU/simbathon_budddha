# Generated by Django 4.2.1 on 2023-06-21 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qnapage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QnaComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenct', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('parent_comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='qnapage.qnacomment')),
                ('qna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qnapage.qna')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
