# Generated by Django 4.0.5 on 2022-08-20 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_boat'),
    ]

    operations = [
        migrations.CreateModel(
            name='fishermen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=2000)),
                ('city', models.CharField(max_length=2000)),
                ('age', models.IntegerField()),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
