# Generated by Django 3.0.8 on 2020-07-16 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200715_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.svg', upload_to='profile_pics'),
        ),
    ]
