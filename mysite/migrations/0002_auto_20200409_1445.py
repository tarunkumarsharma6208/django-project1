# Generated by Django 2.2.10 on 2020-04-09 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.CharField(default='https://p.kindpng.com/picc/s/79-798754_hoteles-y-centros-vacacionales-dish-placeholder-hd-png.png', max_length=500),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(),
        ),
    ]
