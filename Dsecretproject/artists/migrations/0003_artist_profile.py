# Generated by Django 5.1.7 on 2025-07-02 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_alter_artist_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='artist_profiles/'),
        ),
    ]
