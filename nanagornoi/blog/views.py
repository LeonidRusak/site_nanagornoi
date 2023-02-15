from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post, Category


# Create your views here.
def blog_category(request, category):
    # Функция представления списка записей в блоге, выбранных по определенной категории.
    # Отсортированы по времени создания постов, от свежих к старым
    posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog_category.html', context)


def blog_detail(request, pk):
    # Функция представления полной записи блога
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'blog_detail.html', context)


def blog_page(request):
    # Функция представления списка всех записей в блоге.
    # Отсортированные по времени создания постов, от свежих к старым.
    # В функции используется постраничная навигация с помощью класса Paginator
    contact_list = Post.objects.all().order_by('-created_on')
    paginator = Paginator(contact_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog.html', {'page_obj': page_obj, })
