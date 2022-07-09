# Generated by Django 4.0.4 on 2022-07-08 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='total_votes',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='updated_on',
        ),
        migrations.AlterField(
            model_name='poll',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='poll',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='poll',
            name='title',
            field=models.CharField(max_length=256),
        ),
    ]
