# Generated by Django 3.0.5 on 2020-11-17 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='', max_length=70)),
                ('descripcion', models.CharField(default='', max_length=200)),
                ('publicado', models.BooleanField(default=False)),
            ],
        ),
    ]
