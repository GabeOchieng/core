# Generated by Django 3.0.3 on 2020-05-06 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visual',
            fields=[
                ('country', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('case', models.TextField()),
                ('death', models.TextField()),
                ('recovery', models.TextField()),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['country'],
            },
        ),
        migrations.CreateModel(
            name='KenyanCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('cases', models.IntegerField()),
                ('death', models.IntegerField()),
                ('recovery', models.IntegerField()),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date', 'county'],
                'unique_together': {('date', 'county')},
            },
        ),
    ]
