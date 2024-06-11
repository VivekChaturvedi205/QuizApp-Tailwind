# Generated by Django 4.2.13 on 2024-05-27 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=265)),
                ('age', models.IntegerField(default=18)),
                ('createdAt', models.DateTimeField(auto_now=True)),
                ('deletedAtp', models.DateTimeField()),
                ('updatedAt', models.DateTimeField()),
            ],
        ),
    ]
