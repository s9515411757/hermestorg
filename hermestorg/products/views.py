from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import RatingForm
from .models import Rating, Ip, Card, Favourites, Follow
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


User = get_user_model()


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
    card = get_object_or_404(Card, pk=pk)
    ratings = Rating.objects.filter(card=pk)

    rating_list = [rating.star.value for rating in ratings]
    ip = get_client_ip(request)

    if Ip.objects.filter(ip=ip).exists():
        card.number_of_views.add(Ip.objects.get(ip=ip))
    else:
        Ip.objects.create(ip=ip)
        card.number_of_views.add(Ip.objects.get(ip=ip))

    user = User.objects.get(username=request.user.username)
    author = User.objects.get(username=card.author.username)
    follow_list = Follow.objects.filter(user=user, author=author)
    favourites_list = Favourites.objects.filter(user=user, card=pk)

    if follow_list:
        follow_bool = follow_list[0].flag
    else:
        follow_bool = False

    if favourites_list:
        favourites_bool = favourites_list[0].flag
    else:
        favourites_bool = False

    if rating_list:
        rating = sum(rating_list) / len(rating_list)
    else:
        rating = 0

    context = {
        'card': card,
        'number': pk,
        'star_form': RatingForm(),
        'rating': rating,
        'follow_bool': follow_bool,
        'follow_displays': True if request.user.username != card.author.username else False,
        'favourites_bool': favourites_bool

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


@login_required
def add_products(request):
    return redirect('home:index')


@login_required
def add_follow(request, login, id):
    if request.method == 'POST':
        author = User.objects.get(username=login)
        Follow.objects.update_or_create(
            user_id=request.user.id,
            author_id=author.id,
            defaults={"flag": True}
        )
        return redirect('products:products', id)
    else:
        return HttpResponse(status=400)


@login_required
def remove_follow(request, login, id):
    if request.method == 'POST':
        author = User.objects.get(username=login)
        Follow.objects.update_or_create(
            user_id=request.user.id,
            author_id=author.id,
            defaults={"flag": False}
        )
        return redirect('products:products', id)
    else:
        return HttpResponse(status=400)


@login_required
def remove_favourit(request, pk):
    if request.method == 'POST':
        Favourites.objects.update_or_create(
            user_id=request.user.id,
            card_id=pk,
            defaults={"flag": False}
        )
        return redirect('products:products', pk)
    else:
        return HttpResponse(status=400)


@login_required
def add_favourit(request, pk):
    if request.method == 'POST':
        Favourites.objects.update_or_create(
            user_id=request.user.id,
            card_id=pk,
            defaults={"flag": True}
        )
        return redirect('products:products', pk)
    else:
        return HttpResponse(status=400)