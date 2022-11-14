from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact, Post
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-published_date')
    paginator = Paginator(posts, 4)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    return render(request, 'home.html', {'page': page})

def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post.html', {'post': post})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            newform = Contact(
                name=form.cleaned_data['name'], 
                email_address=form.cleaned_data['email_address'], 
                phone_number=form.cleaned_data['phone_number'], 
                message=form.cleaned_data['message']
            )
            newform.save()
            messages.success(request, 'Mensagem enviado com sucesso!')
            return redirect(contact)
        else:
            messages.error(request, 'Erro ao enviar mensagem!')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form':form})

def handler404(request, exception):
    return render(request, '404.html')

def handler500(request):
    return render(request, '500.html')
