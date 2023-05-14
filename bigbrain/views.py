from django.http import HttpResponse


# Test
def index():
    return HttpResponse("Hello, world. You're at the polls index.")
