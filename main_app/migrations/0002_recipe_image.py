# Generated by Django 4.1.1 on 2022-09-30 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='', upload_to='main_app/static/uploads/'),
        ),
    ]