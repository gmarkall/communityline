# Generated by Django 4.1.7 on 2023-03-12 17:34

import callrouting.models
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_progress', models.BooleanField(default=False)),
                ('last_sent', models.DateField(default=callrouting.models.yesterday)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('incoming_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Incoming Number')),
                ('greeting', models.CharField(max_length=200)),
                ('default_action', models.CharField(choices=[('Voicemail', 'Voicemail'), ('Default Destination', 'Default Destination')], default='Default Destination', max_length=25)),
                ('default_destination', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Default Destination')),
                ('voicemail_email', models.EmailField(default='default@domain.local', max_length=254)),
                ('voicemail_greeting', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254)),
                ('send_emails', models.BooleanField(default=True)),
                ('user_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='callrouting.usergroup')),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=10)),
                ('start_time', models.IntegerField(choices=[(6, '6AM'), (7, '7AM'), (8, '8AM'), (9, '9AM'), (10, '10AM'), (11, '11AM'), (12, 'Midday'), (13, '1PM'), (14, '2PM'), (15, '3PM'), (16, '4PM'), (17, '5PM'), (18, '6PM'), (19, '7PM'), (20, '8PM'), (21, '9PM'), (22, '10PM'), (23, '11PM')])),
                ('end_time', models.IntegerField(choices=[(6, '6AM'), (7, '7AM'), (8, '8AM'), (9, '9AM'), (10, '10AM'), (11, '11AM'), (12, 'Midday'), (13, '1PM'), (14, '2PM'), (15, '3PM'), (16, '4PM'), (17, '5PM'), (18, '6PM'), (19, '7PM'), (20, '8PM'), (21, '9PM'), (22, '10PM'), (23, '11PM')])),
                ('user_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='callrouting.usergroup')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='callrouting.volunteer')),
            ],
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('sid', models.CharField(max_length=34, primary_key=True, serialize=False, verbose_name='Call SID')),
                ('caller_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Caller Number')),
                ('called_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Called Number')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='Time')),
                ('recording_begun', models.BooleanField(default=False, verbose_name='Recording begun')),
                ('recording_received', models.BooleanField(default=False, verbose_name='Recording received')),
                ('recording_url', models.URLField(null=True, verbose_name='Recording URL')),
                ('transcription_received', models.BooleanField(default=False, verbose_name='Transcription received')),
                ('transcription_successful', models.BooleanField(default=False, verbose_name='Transcription successful')),
                ('transcription_text', models.CharField(max_length=8192, null=True, verbose_name='Transcription text')),
                ('email_attempted', models.BooleanField(default=False, verbose_name='Email attempted')),
                ('email_send_time', models.DateTimeField(null=True, verbose_name='Email send time')),
                ('email_send_finished', models.BooleanField(default=False, verbose_name='Email send finished')),
                ('user_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='callrouting.usergroup')),
            ],
        ),
    ]