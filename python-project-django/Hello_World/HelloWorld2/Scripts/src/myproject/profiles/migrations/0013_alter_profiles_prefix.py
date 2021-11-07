# Generated by Django 3.2.9 on 2021-11-05 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_alter_profiles_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='Prefix',
            field=models.CharField(choices=[('Ms. ', 'Ms. '), ('Mr. ', 'Mr. '), ('Mrs. ', 'Mrs. ')], default='', max_length=60),
        ),
    ]
