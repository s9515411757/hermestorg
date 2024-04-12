from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RatingForm
from .models import Rating, Ip, Card


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):
    cards = Card.objects.all()

    context = {
        'cards': cards
    }
    return render(request, 'products/index.html', context)


def products(request, pk):
    card = Card.objects.get(pk=pk)
    rating = Rating.objects.filter(card=card.id)
    result = [rating.star.value for rating in rating]


    ip = get_client_ip(request)

    if Ip.objects.filter(ip=ip).exists():
        card.number_of_views.add(Ip.objects.get(ip=ip))
    else:
        Ip.objects.create(ip=ip)
        card.number_of_views.add(Ip.objects.get(ip=ip))

    context = {
        'card': card,
        'number': pk,
        'star_form': RatingForm(),
        'rating': sum(result) / len(result)

    }

    return render(request, 'products/products.html', context)


def add_star_rating(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=get_client_ip(request),
                card_id=int(request.POST.get("card")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=400)


def add_products(request):
    return redirect('home:index')