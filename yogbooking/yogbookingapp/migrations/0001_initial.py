# Generated by Django 3.0.7 on 2021-01-09 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('img1', models.ImageField(upload_to='yogbookingapp/images')),
                ('img2', models.ImageField(upload_to='yogbookingapp/images')),
                ('text', models.CharField(default='', max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=20)),
                ('no_of_students', models.IntegerField(default=0)),
                ('date_of_event', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('description', models.CharField(default='', max_length=1000)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('name', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default='0')),
                ('description', models.CharField(default='', max_length=1000)),
                ('id', models.CharField(default='', max_length=20, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='yogbookingapp/images')),
            ],
        ),
        migrations.CreateModel(
            name='Upcommingevent',
            fields=[
                ('name', models.CharField(default='', max_length=50)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='yogbookingapp/images')),
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
    ]