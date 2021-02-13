from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = 'Creates a dummy blog'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='How many blog sets to create')
        # parser.add_argument("-d", "--delay", type=int, help='')  # -d = command line, --deplay = in handle() method

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write(f"It's now {time}")
