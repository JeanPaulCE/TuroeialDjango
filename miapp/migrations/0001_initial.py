# Generated by Django 3.2.6 on 2021-08-16 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='visita', max_length=120)),
                ('edad', models.IntegerField(default=18)),
            ],
        ),
    ]
