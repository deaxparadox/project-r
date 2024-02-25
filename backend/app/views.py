from django.shortcuts import render

from . import forms

def search_view(request):
    form = forms.SearchForm()
    return render(
        request,
        "app/index.html",
        {
            "form": form
        }
    )