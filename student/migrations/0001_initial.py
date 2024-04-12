# Generated by Django 4.2.11 on 2024-04-12 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stu_Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('dateOfBirth', models.DateField()),
                ('status', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/img')),
                ('cls', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.stu_class')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
