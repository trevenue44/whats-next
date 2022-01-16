# Generated by Django 3.2.9 on 2022-01-16 07:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
