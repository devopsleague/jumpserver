# Generated by Django 2.2.13 on 2020-08-19 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_auto_20200814_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('Admin', 'System administrator'), ('Auditor', 'System auditor'), ('User', 'User'), ('App', 'Application')], default='User', max_length=10, verbose_name='Role'),
        ),
    ]
