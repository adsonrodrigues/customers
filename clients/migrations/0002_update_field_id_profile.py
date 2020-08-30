# Generated by Django 3.1 on 2020-08-30 09:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_create_model_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.CharField(default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]