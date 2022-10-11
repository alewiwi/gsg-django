# Generated by Django 4.1 on 2022-10-06 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('cdate', models.DateField(auto_now=True)),
                ('visible', models.BooleanField()),
            ],
        ),
    ]
