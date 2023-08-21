import os

from api.models import Service, ServiceHashtag
from django.conf import settings
from django.core.management.base import BaseCommand
from helpers.main import get_categories_from_file


class Command(BaseCommand):
    help = "Заполняем категории и их хештеги"

    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR, r'helpers\категории.docx')

        categories = get_categories_from_file(path)
        for item in categories:
            obj = Service.objects.create(name=item)
            obj.save()

            print(f'{item} was created', end="")

            for tag in categories[item]:
                tag_obj = ServiceHashtag.objects.create(
                    name=tag,
                    service=obj
                )
                tag_obj.save()
                print(tag, sep=" ")


