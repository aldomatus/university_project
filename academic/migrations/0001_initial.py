# Generated by Django 3.2 on 2021-04-29 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('duration', models.PositiveSmallIntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('code', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('credits', models.PositiveSmallIntegerField()),
                ('teacher', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('dni', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('first_last_name', models.CharField(max_length=35)),
                ('second_last_name', models.CharField(max_length=35)),
                ('name', models.CharField(max_length=35)),
                ('date_of_birth', models.DateField()),
                ('sex', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='F', max_length=1)),
                ('vigencia', models.BooleanField(default=True)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.career')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('enrollment_date', models.DateField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.student')),
            ],
        ),
    ]
