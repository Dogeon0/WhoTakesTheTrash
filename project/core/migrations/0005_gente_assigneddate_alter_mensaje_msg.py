# Generated by Django 5.0.4 on 2024-07-11 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_mensaje_msg'),
    ]

    operations = [
        migrations.AddField(
            model_name='gente',
            name='assignedDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='msg',
            field=models.CharField(max_length=150),
        ),
    ]
