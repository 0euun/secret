# Generated by Django 5.2.3 on 2025-07-07 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='language',
            field=models.IntegerField(choices=[(1, 'KOR'), (2, 'ENG')], null=True),
        ),
    ]
