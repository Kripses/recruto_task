from django.shortcuts import render


def get_view(request):
    context = {}
    return render(request, 'get_template.html', context=context)
