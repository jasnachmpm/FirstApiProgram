# Generated by Django 4.2.7 on 2023-12-14 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restApiApp', '0002_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(default='Image/None/Noimg.jpg', upload_to='Images/'),
        ),
    ]
