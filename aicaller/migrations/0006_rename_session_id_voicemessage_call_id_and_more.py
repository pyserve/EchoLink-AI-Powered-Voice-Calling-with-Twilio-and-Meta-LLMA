# Generated by Django 5.0.7 on 2024-07-18 04:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("aicaller", "0005_alter_voicechat_lead"),
    ]

    operations = [
        migrations.RenameField(
            model_name="voicemessage",
            old_name="session_id",
            new_name="call_id",
        ),
        migrations.RemoveField(
            model_name="voicechat",
            name="session_id",
        ),
    ]