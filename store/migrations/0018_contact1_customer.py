# Generated by Django 3.1.5 on 2021-04-07 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_remove_contact1_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact1',
            name='customer',
            field=models.ForeignKey(default=34, on_delete=django.db.models.deletion.CASCADE, to='store.customer'),
            preserve_default=False,
        ),
    ]
