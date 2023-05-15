from django.shortcuts import render

# Create your views here.
def celebration(request):
    return render(request, 'gallery/celebration.html')

def product(request):
    return render(request,'gallery/landmark.html')

def food(request):
    return render(request,'gallery/food.html')
