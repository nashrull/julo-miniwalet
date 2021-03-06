# Generated by Django 3.0 on 2021-09-09 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='koran',
            name='deposit_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='koran',
            name='deposit_by',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='koran',
            name='withdrawal_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='koran',
            name='withdrawal_by',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
