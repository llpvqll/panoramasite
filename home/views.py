from django.shortcuts import render

# Create your views here.


def main_view(request):
    template_name = 'home/base.html'
    context = {}
    return render(request, template_name, context)

