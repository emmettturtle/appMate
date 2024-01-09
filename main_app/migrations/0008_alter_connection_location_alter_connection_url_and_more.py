# Generated by Django 4.2.8 on 2024-01-09 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_interaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='location',
            field=models.CharField(blank=True, max_length=50, verbose_name='Place/Event Met'),
        ),
        migrations.AlterField(
            model_name='connection',
            name='url',
            field=models.CharField(blank=True, max_length=50, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='interaction',
            name='description',
            field=models.TextField(max_length=200, verbose_name='Add Interaction'),
        ),
    ]
