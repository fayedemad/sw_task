# Generated by Django 5.0.9 on 2024-10-02 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='picture',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='categories'),
        ),
    ]
