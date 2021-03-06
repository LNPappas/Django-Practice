# Generated by Django 2.2.5 on 2019-09-25 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=264, unique=True)),
                ('last', models.CharField(max_length=264, unique=True)),
                ('email', models.EmailField(max_length=264, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=264, unique=True),
        ),
    ]
