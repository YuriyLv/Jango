# Generated by Django 4.1.7 on 2023-03-16 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_img_alter_category_category_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.RemoveField(
            model_name='post',
            name='img',
        ),
    ]