# Generated by Django 3.0.8 on 2020-07-29 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formcms', '0004_auto_20200729_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='employee_image'),
        ),
    ]
