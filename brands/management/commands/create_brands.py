from django.core.management.base import BaseCommand
from brands.models import Brand

BRANDS = [
    "Nike",
    "Adidas",
    "Puma",
    "Converse",
    "Vans",
    "Mizuno",
    "Levi's",
    "Wrangler",
    "Calvin Klein",
    "Tommy Hilfiger",
    "Quiksilver",
    "Billabong",
    "Champion",
    "Hollister",
    "Gap",
    "Thrasher",
    "New Era",
    "Ray-Ban",
    "Oakley",
    "TXC",
]

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        for brand in BRANDS:
            Brand.objects.create(name=brand) 

        self.stdout.write(self.style.SUCCESS("MARCAS CRIADAS COM SUCESSO!"))
