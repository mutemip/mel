# Generated by Django 4.1.1 on 2022-09-21 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home', models.CharField(default='Kerico', max_length=255)),
                ('age', models.IntegerField(default=1)),
                ('salary', models.IntegerField(default=10000)),
            ],
        ),
    ]