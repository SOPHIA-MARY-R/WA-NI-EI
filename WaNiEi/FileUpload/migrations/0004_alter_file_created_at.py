# Generated by Django 4.1.1 on 2022-10-03 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FileUpload', '0003_alter_file_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
