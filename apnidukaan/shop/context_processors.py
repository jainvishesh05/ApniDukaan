from .models import Categories

def all_categories(request):
    return {
        'all_categories': Categories.objects.all()
    } 