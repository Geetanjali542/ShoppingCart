
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from carts.models import CartItem
from carts.views import _cart_id
from .models import Product
from category.models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator 
from django.db.models import Q

# Create your views here.

def store(request, category_slug=None): #the category_slug is set to None by default when no value comes
  categories = None
  products = None 
  if category_slug is not None: #it means if we are receving the category_slug then, this whole if condition is for the  'All category option" and in that filtering the objects and also the context processor thing is used for "All category option' for iterating the categories objects which are category_slug
    categories = get_object_or_404(Category, slug = category_slug )
    products = Product.objects.filter(category = categories, is_available = True).order_by('id') #here id is pre defined keyword and can be used for iterating 
    paginator = Paginator(products, 3)  #it means when we click on category and after that only one product will be viewed on one page and paginator will be available for iterating 



    page = request.GET.get('page')   # we are fetching the data from the url query in url  -> http://127.0.0.1:8000/store/?page=2 
    paged_products = paginator.get_page(page)  # it will render the page which is coming from the query of url -> http://127.0.0.1:8000/store/?page=2  page number is 2

    product_count = products.count()  #it gives the product count

  else:  #this is for when the category_slug is none
    products = Product.objects.all().filter(is_available=True).order_by('id')
    paginator = Paginator(products, 3) #it means three products will be visible in one page in the whole page
    page = request.GET.get('page')  #Requested page number 
    paged_products = paginator.get_page(page)   # it will render the requested page number
    product_count = products.count()

  context = {
    'products': paged_products,
    'paged_count':product_count,
  }

  return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug = product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()    
    except Exception as e:
        raise e 
    context = {
        'single_product':single_product,
        'in_cart':in_cart,
    }
    return render(request, 'store/product_detail.html', context)


def search(request):
  if 'keyword' in request.GET:
    keyword = request.GET.get('keyword')
    if keyword:
      products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains = keyword)) #if description or product_name contains keyword then store the product in products.
      product_count = products.count()
    
  context = {
    'products': products,
    'product_count': product_count,
  }

  return render(request, 'store/store.html', context)




  

