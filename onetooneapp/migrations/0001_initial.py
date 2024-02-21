# Generated by Django 4.2.7 on 2023-11-20 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50)),
                ('student_roll', models.IntegerField()),
                ('student_email', models.EmailField(max_length=254)),
                ('student_mobile', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('course_fee', models.IntegerField()),
                ('course_duration', models.IntegerField()),
                ('abc', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='onetooneapp.student')),
            ],
        ),
    ]
