# Generated by Django 3.0.8 on 2020-07-15 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20200630_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profile_picture',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
