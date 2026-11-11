import csv
from datetime import datetime

from django.core.management.base import BaseCommand

from phones.models import Phone


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('phones.csv', encoding='utf-8', newline='') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';')

            for row in reader:
                Phone.objects.update_or_create(
                    id=int(row['id']),
                    defaults={
                        'name': row['name'],
                        'image': row['image'],
                        'price': int(row['price']),
                        'release_date': datetime.strptime(
                            row['release_date'], '%Y-%m-%d'
                        ).date(),
                        'lte_exists': row['lte_exists'].strip().lower() == 'true',
                    },
                )

        self.stdout.write(self.style.SUCCESS('Телефоны загружены в базу'))