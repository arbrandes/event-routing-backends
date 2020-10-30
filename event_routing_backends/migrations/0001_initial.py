# Generated by Django 2.2.16 on 2020-10-01 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import event_routing_backends.utils.fields
import jsonfield.encoder


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RouterConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_date', models.DateTimeField(auto_now_add=True, verbose_name='Change date')),
                ('enabled', models.BooleanField(default=False, verbose_name='Enabled')),
                ('backend_name', models.CharField(help_text='Name of the tracking backend on which this router should be applied.<br/>Please note that this field is <b>case sensitive.</b>', max_length=50, verbose_name='Backend name')),
                ('configurations', event_routing_backends.utils.fields.EncryptedJSONField(dump_kwargs={'cls': jsonfield.encoder.JSONEncoder, 'separators': (',', ':')}, load_kwargs={})),
                ('changed_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Changed by')),
            ],
            options={
                'verbose_name': 'Router Configuration',
                'verbose_name_plural': 'Router Configurations',
            },
        ),
    ]
