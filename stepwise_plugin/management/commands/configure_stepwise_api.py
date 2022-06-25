from django.core.management.base import BaseCommand

from ...models import Configuration


class Command(BaseCommand):  # lint-amnesty, pylint: disable=missing-class-docstring
    help = "Create or update a Stepwise API configuration."

    def add_arguments(self, parser):
        parser.add_argument(
            "--host",
            dest="host",
            default="https://stepwiseai01.querium.com/webMathematica/api/",
            required=False,
            nargs=1,
            help="URL to the Stepwise API host. Default: https://stepwiseai01.querium.com/webMathematica/api/",
        )
        parser.add_argument(
            "--environment",
            dest="environment",
            default="Production",
            required=False,
            nargs=1,
            help="Which Open edX environment to configure. Options: Development, Testing / QA, Production,  Default: Production",
        )

    def handle(self, *args, **options):

        Configuration.objects.update_or_create(type=options.get("environment"), stepwise_host=options.get("host"))
