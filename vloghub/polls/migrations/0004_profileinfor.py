# Generated by Django 4.1 on 2023-07-04 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0003_alter_profile_follows_vlog"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProfileInfor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=50)),
                ("About", models.TextField(max_length=500)),
                ("Company", models.CharField(max_length=50)),
                ("Job", models.CharField(max_length=50)),
                ("Country", models.CharField(max_length=50)),
                ("Address", models.CharField(max_length=100)),
                ("Phone", models.CharField(max_length=12)),
                ("Email", models.EmailField(max_length=254)),
                ("Twitter_Profile", models.URLField(blank=True)),
                ("Facebook_Profile", models.URLField(blank=True)),
                ("Instagram_Profile", models.URLField(blank=True)),
                ("Linkedin_Profile", models.URLField(blank=True)),
                (
                    "profile",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="polls.profile"
                    ),
                ),
            ],
        ),
    ]
