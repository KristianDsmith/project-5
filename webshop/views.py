from django.shortcuts import render


def custom_handler404(request, exception):
    return render(request, '404.html', status=404)


handler404 = 'webshop.views.custom_handler404'
