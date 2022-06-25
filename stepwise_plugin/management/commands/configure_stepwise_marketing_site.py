from django.core.management.base import BaseCommand

from ...models import MarketingSites


class Command(BaseCommand):  # lint-amnesty, pylint: disable=missing-class-docstring
    help = "Create or update a Stepwise marketing site configuration."

    def add_arguments(self, parser):
        parser.add_argument(
            "--language",
            dest="language",
            default="en",
            required=False,
            nargs=1,
            help="A language code. Examples: en, en-US, es, es-419, es-MX. Default: en",
        )
        parser.add_argument(
            "--province",
            dest="province",
            required=False,
            nargs=1,
            help="A sub-region for the language code. Example: for language code en-US valid possibles include TX, FL, CA, DC, KY, etc.",
        )
        parser.add_argument(
            "--site_url",
            dest="site_url",
            default="https://stepwisemath.ai/",
            required=False,
            nargs=1,
            help="Base URL for the marketing site for this language. Default: https://stepwisemath.ai/",
        )

    def handle(self, *args, **options):

        MarketingSites.objects.update_or_create(
            language=options.get("language"),
            province=options.get("province"),
            site_url=options.get("site_url"),
        )
