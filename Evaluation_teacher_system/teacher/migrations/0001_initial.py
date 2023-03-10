# Generated by Django 4.1.3 on 2022-12-23 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subject', '0001_initial'),
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('rate_avg', models.FloatField(default=0, max_length=2)),
                ('teacher_id', models.CharField(max_length=6, unique=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.college')),
                ('subject_id', models.ManyToManyField(to='subject.subject')),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
    ]
