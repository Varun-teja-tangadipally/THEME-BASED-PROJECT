# Generated by Django 2.1.7 on 2019-03-29 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_corporate_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='individual',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]