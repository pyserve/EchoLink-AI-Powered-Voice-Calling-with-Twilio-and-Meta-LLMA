# Generated by Django 5.0.7 on 2024-07-18 04:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("aicaller", "0002_voicemessage_session_id_alter_voicechat_ai_caller_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="voicechat",
            name="call_id",
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="voicechat",
            name="session_id",
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="voicemessage",
            name="session_id",
            field=models.CharField(max_length=255),
        ),
    ]
