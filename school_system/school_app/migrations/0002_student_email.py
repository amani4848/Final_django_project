# Generated by Django 5.0.7 on 2024-07-28 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]