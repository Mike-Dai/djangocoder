# Generated by Django 2.1.7 on 2019-03-04 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_img_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img_link',
            field=models.CharField(default='images/logo.jpeg', max_length=255),
        ),
    ]