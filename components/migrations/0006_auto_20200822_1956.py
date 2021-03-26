# Generated by Django 3.1 on 2020-08-22 11:56

from django.db import migrations
import simplepro.components.fields


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0005_imagemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='f2',
            field=simplepro.components.fields.ImageField(default=123, max_length=128, verbose_name='图片上传'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='f1',
            field=simplepro.components.fields.ImageField(max_length=128, verbose_name='图片上传'),
        ),
    ]