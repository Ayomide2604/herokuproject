from . models import *
def categories(request):
    categories = Category.objects.order_by('name')
    return {
        'categories': categories,

    }