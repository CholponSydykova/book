from django.shortcuts import render, HttpResponse

def bookshelf(request):
    return HttpResponse("Bookshelf!")

def test(request):
    return render(request, "test.html")

