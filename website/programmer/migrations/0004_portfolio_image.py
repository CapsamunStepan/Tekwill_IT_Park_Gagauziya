# Generated by Django 4.2.4 on 2023-09-14 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmer', '0003_remove_portfolio_surname_portfolio_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(default='programmer/static/programmer/images/no-image.png', upload_to='programmer/static/programmer/images'),
        ),
    ]
