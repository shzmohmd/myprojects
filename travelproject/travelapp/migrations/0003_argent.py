# Generated by Django 4.1.7 on 2023-03-04 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Argent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nam', models.CharField(max_length=150)),
                ('im', models.ImageField(upload_to='argpic')),
                ('des', models.TextField()),
            ],
        ),
    ]
