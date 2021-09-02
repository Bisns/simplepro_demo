# Generated by Django 3.2.6 on 2021-08-20 12:25

from django.db import migrations, models
import django.db.models.deletion
import simplepro.components.fields


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0027_native'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(max_length=100, verbose_name='商品分类'),
        ),
        migrations.CreateModel(
            name='FilterMultiple',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', simplepro.components.fields.CharField(blank=True, max_length=64, null=True, verbose_name='名称')),
                ('category', simplepro.components.fields.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='demo.productcategory', verbose_name='商品品类')),
            ],
            options={
                'verbose_name': '下拉框多选',
                'verbose_name_plural': '下拉框多选',
            },
        ),
    ]