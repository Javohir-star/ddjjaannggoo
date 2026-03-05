from django.shortcuts import render
from .models import Author

def author_list(request):
    authors = Author.objects.all()

    context= {
        "authors":authors,
    }

    return render(request, "authors.html", context=context)