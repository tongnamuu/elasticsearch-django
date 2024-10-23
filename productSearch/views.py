from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return HttpResponse("main index")

def error_404_view(request, exception):
    return HttpResponseNotFound("404 error")