# Generated by Django 4.1 on 2022-10-15 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_teacher_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='title',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
