# Generated by Django 2.0.13 on 2019-05-25 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text2',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
