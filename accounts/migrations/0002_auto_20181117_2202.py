# Generated by Django 2.1.3 on 2018-11-17 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity_Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=150)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('activity', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
