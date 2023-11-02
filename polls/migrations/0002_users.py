# Generated by Django 4.2.5 on 2023-10-06 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('years', models.IntegerField(default=0)),
                ('data', models.DateField(verbose_name='date login')),
                ('abort', models.BooleanField(default=False)),
            ],
        ),
    ]
