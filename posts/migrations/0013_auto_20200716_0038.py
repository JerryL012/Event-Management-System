# Generated by Django 3.0.8 on 2020-07-16 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200715_2336'),
        ('posts', '0012_auto_20200715_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]