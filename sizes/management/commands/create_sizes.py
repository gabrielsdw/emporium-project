from django.core.management.base import BaseCommand
from sizes.models import Size

SIZES = [
    '34',
    '35',
    '36',
    '37',
    '38',
    '39',
    '40',
    '41',
    '42',
    '43',
    '44',
    '45',
    'P',
    'M',
    'G',
    'GG',
]

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        for size in SIZES:
            Size.objects.create(name=size) 

        self.stdout.write(self.style.SUCCESS("TAMANHOS CRIADOS COM SUCESSO!"))
