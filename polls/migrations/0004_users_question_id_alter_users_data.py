# Generated by Django 4.2.6 on 2023-10-25 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_users_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='question_ID',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='users',
            name='data',
            field=models.DateField(),
        ),
    ]
