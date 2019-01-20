# Generated by Django 2.1.5 on 2019-01-18 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190118_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64, verbose_name='First name')),
                ('last_name', models.CharField(max_length=64, verbose_name='Last name')),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('break_time', models.SmallIntegerField(default=60)),
                ('shift_type', models.SmallIntegerField(choices=[(1, '5:00:00 AM,1:30:00 PM'), (2, '1:00:00 PM,9:30:00 PM'), (3, '9:00:00 PM,5:30:00 AM')], default=1)),
                ('store_type', models.SmallIntegerField(choices=[(1, '5:00:00 AM,1:30:00 PM'), (2, '1:00:00 PM,9:30:00 PM'), (3, '9:00:00 PM,5:30:00 AM')], default=1)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Employee')),
            ],
        ),
    ]