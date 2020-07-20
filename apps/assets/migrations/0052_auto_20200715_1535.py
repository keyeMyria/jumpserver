# Generated by Django 2.2.10 on 2020-07-15 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0051_auto_20200713_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commandfilter',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Name'),
        ),
        migrations.AlterUniqueTogether(
            name='commandfilter',
            unique_together={('org_id', 'name')},
        ),
    ]