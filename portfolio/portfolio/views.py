from django.http import HttpResponse


def about(request):
    return HttpResponse("this is our about page!!!")
    