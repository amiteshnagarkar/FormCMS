# Generated by Django 3.0.8 on 2020-07-30 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formcms', '0005_auto_20200729_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
