from django.views import generic
from products import models
from brands.models import Brand

class ProductListView(generic.ListView):
    model = models.Product
    template_name = 'products_list.html'
    context_object_name = 'products'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.brand = kwargs.get('brand', 'wwwwwww')
        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        context['selected_mode'] = self.request.GET.get('mode')
        context['selected_brand'] = self.request.GET.get('brand')
        return context
    

    def get_queryset(self):
        products = models.Product.objects.all()
        
        brand = self.request.GET.get('brand', '')
        mode = self.request.GET.get('mode', '')
        search = self.request.GET.get('search', '')
        
        if search:
            return products.filter(name__icontains=search)
       
        if brand:
            products = products.filter(brand__name=brand)
        
        match mode:
            case "menu_order":
                return products.order_by('name')
            case "price":
                return products.order_by('selling_price')
            case "price-desc":
                return products.order_by('-selling_price')
        return products
        
    
class ProductDetailView(generic.DetailView):
    model = models.Product
    template_name = 'products_detail.html'
    context_object_name = 'product'