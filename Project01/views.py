from django.http import HttpResponse


def greeting(request):  # First view
    return HttpResponse("Hi there! This is a very simple page with Django!")


def bye(request):  # Second view
    return HttpResponse("Bye bye!")