# Generated by Django 3.2.7 on 2022-03-31 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20220331_1340'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsmodel',
            options={'ordering': ('-created_at',)},
        ),
        migrations.RenameField(
            model_name='newsmodel',
            old_name='cover_photo',
            new_name='thumbnail',
        ),
    ]
