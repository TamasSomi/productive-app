# Generated by Django 3.2.23 on 2024-01-03 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='image',
            field=models.ImageField(blank=True, default='../default_post_wadwig', upload_to='images/'),
        ),
    ]
