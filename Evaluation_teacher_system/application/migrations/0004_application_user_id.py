# Generated by Django 4.1.3 on 2023-03-19 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_alter_application_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='user_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]