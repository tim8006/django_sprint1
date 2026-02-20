from django.shortcuts import render

posts = [
    {
        'id': 0,
        'location': 'Остров отчаянья',
        'date': '30 сентября 1659 года',
        'category': 'travel',
        'text': 'Наш корабль потерпел крушение...',
    },
    {
        'id': 1,
        'location': 'Остров отчаянья',
        'date': '1 октября 1659 года',
        'category': 'not-my-day',
        'text': 'Проснувшись поутру...',
    },
]

def index(request):
    context = {'posts': posts}
    return render(request, 'index.html', context)

def post_detail(request, id):
    post = posts[id]
    context = {'post': post}
    return render(request, 'detail.html', context)

def category_posts(request, category_slug):
    context = {'category_slug': category_slug}
    return render(request, 'category.html', context)
