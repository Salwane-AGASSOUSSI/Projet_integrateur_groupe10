# Generated by Django 4.2.2 on 2023-06-26 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_etudiant_username_alter_etudiant_matricule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiant',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='etudiant',
            name='username',
        ),
    ]