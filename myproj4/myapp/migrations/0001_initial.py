# Generated by Django 5.0.6 on 2024-06-17 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(max_length=200)),
                ('age', models.IntegerField()),
                ('mobile', models.CharField(max_length=10)),
                ('dob', models.DateField()),
            ],
        ),
    ]
