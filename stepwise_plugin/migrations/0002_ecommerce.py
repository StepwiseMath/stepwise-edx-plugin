# Generated by Django 2.2.13 on 2020-08-05 17:13

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import opaque_keys.edx.django.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("stepwise_plugin", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="EcommerceConfiguration",
            fields=[
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="modified"
                    ),
                ),
                (
                    "course_id",
                    opaque_keys.edx.django.models.CourseKeyField(
                        default=None,
                        help_text="Stepwise Math Course Key (Opaque Key). Based on Institution, Course, Section identifiers. Example: course-v1:edX+DemoX+Demo_Course",
                        max_length=255,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "payment_deadline_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="The date after which the paywall will rise for enrolled students who have not yet paid.",
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Stepwise Math E-Commerce Configuration",
                "verbose_name_plural": "Stepwise Math E-Commerce Configurations",
            },
        ),
        migrations.CreateModel(
            name="EcommerceEOPWhitelist",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="modified"
                    ),
                ),
                ("user_email", models.EmailField(max_length=254, unique=True)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("eop_student", "EOP Student"),
                            ("tester", "Stepwise Math Tester"),
                            ("free_retake", "Free Retake"),
                        ],
                        default="eop_student",
                        help_text="Type of E-Commerce whitelist user.",
                        max_length=24,
                    ),
                ),
            ],
            options={
                "verbose_name": "Stepwise Math E-Commerce Payment Exemption",
                "verbose_name_plural": "Stepwise Math E-Commerce Payment Exemptions",
            },
        ),
    ]
