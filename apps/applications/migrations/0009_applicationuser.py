# Generated by Django 3.1.6 on 2021-06-23 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0070_auto_20210426_1515'),
        ('applications', '0008_auto_20210104_0435'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationUser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('assets.systemuser',),
        ),
    ]
