# Generated by Django 4.2.2 on 2023-06-23 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_etudiant_admin_etudiant_is_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiant',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='etudiant',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='etudiant',
            name='staff',
        ),
    ]