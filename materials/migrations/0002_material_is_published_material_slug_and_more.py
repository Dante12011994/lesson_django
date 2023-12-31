# Generated by Django 4.2.3 on 2023-07-29 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='опубликовано'),
        ),
        migrations.AddField(
            model_name='material',
            name='slug',
            field=models.CharField(default=1, max_length=150, verbose_name='slug'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='material',
            name='views_count',
            field=models.IntegerField(default=0, verbose_name='просмотры'),
        ),
    ]
