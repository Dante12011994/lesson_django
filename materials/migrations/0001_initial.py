# Generated by Django 4.2.3 on 2023-07-18 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название')),
                ('body', models.TextField(verbose_name='содержимое')),
            ],
            options={
                'verbose_name': 'материал',
                'verbose_name_plural': 'материалы',
            },
        ),
    ]
