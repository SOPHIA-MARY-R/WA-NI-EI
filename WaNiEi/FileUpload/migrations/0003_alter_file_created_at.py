# Generated by Django 4.1.1 on 2022-10-02 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FileUpload', '0002_file_delete_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
