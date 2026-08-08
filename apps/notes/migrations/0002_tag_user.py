# Generated manually for StudySync backend stabilization.
# Makes Tag user-specific: every tag now belongs to a user.
# The notes_tag table is empty in the development database, so no
# data backfill is required.

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="tag",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tags",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(max_length=50),
        ),
        migrations.AddConstraint(
            model_name="tag",
            constraint=models.UniqueConstraint(
                fields=("user", "name"),
                name="unique_tag_name_per_user",
            ),
        ),
    ]
