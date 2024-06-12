from django.views import generic
from products import models
from brands.models import Brand

class ProductListView(generic.ListView):
    model = models.Product
    template_name = 'products_list.html'
    context_object_name = 'products'
    paginate_by = 9


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
        category = self.request.GET.get('category_id', '')
        
        
           
        if search:
            products = products.filter(name__icontains=search)
       
        if brand:
            products = products.filter(brand__name=brand)

        if category:
            products = products.filter(category__id=category)
        
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