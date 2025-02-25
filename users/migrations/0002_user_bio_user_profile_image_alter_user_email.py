# Generated by Django 5.1.6 on 2025-02-25 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.CharField(default='Hello World', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
