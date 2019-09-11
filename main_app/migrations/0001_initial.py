# Generated by Django 2.2.3 on 2019-09-11 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('issue', models.IntegerField()),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('publishdate', models.DateField()),
            ],
        ),
    ]
