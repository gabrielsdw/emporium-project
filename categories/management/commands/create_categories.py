from django.core.management.base import BaseCommand
from categories.models import Category 

CATEGORIES = {
    '1': 'Tênis',
    '2': 'Boné',
    '3': 'Blusa',
    '4': 'Moletom',
    '5': 'Calça',
    '6': 'Short',
    '7': 'Acessório',
}


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        
        for id, category in CATEGORIES.items():
            Category.objects.create(id=id, name=category)

        self.stdout.write(self.style.SUCCESS("CATEGORIAS CRIADAS COM SUCESSO!"))
