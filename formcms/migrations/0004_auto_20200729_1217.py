# Generated by Django 3.0.8 on 2020-07-29 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formcms', '0003_auto_20200728_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
