# Generated by Django 2.2.9 on 2020-01-17 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='age',
        ),
        migrations.AddField(
            model_name='actor',
            name='birth_date',
            field=models.DateField(default='2000-01-01'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='cast',
            field=models.ManyToManyField(related_name='movies', to='movies.Actor'),
        ),
    ]
