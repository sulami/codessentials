from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from posts.models import Post
from datetime import timedelta

class Command(BaseCommand):
    help = 'Delete old posts without votes'

    def handle(self, *args, **options):
        count = 0
        for p in Post.objects.all().filter(pub_date__lte=timezone.now() -
                                           timedelta(days=30)):
            if p.votes < 10:
                count += 1
                p.delete()
        print("Deleted %d posts." % count)

