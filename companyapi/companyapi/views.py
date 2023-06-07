from django.http import HttpResponse,JsonResponse

def home_page(request):   #function based view
    print("home page requested")
    friends=[
        'ankit',
        'ravi',
        'uttam'
    ]
    return JsonResponse(friends,safe=False) # it should be map by urls.py