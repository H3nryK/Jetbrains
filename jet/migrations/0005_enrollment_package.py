# Generated by Django 5.0.6 on 2024-07-11 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jet', '0004_alter_contact_email_alter_enrollment_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='package',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
