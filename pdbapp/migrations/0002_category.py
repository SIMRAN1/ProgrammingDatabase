# Generated by Django 2.1 on 2018-08-09 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdbapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]