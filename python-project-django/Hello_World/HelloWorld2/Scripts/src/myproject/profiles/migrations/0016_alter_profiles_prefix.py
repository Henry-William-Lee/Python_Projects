# Generated by Django 3.2.9 on 2021-11-05 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_alter_profiles_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='Prefix',
            field=models.CharField(choices=[('Mrs. ', 'Mrs. '), ('Mr. ', 'Mr. '), ('Ms. ', 'Ms. ')], default='', max_length=60),
        ),
    ]