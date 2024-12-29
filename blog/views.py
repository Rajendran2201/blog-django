from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from blog.models import Post, AboutUs
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm

# Create your views here.

all_posts = Post.objects.all()
def index(request):
  blog_title = "Raj's Blog Posts"

  # Paginate
  paginator = Paginator(all_posts, 5)
  page_number = request.GET.get('page')
  posts =  paginator.get_page(page_number)
  return render(request, 'index.html', {'blog_title': blog_title, 'posts': posts})

def detail(request, slug):

  try:
    # getting data by id from the model
    post = Post.objects.get(slug=slug)
    related_posts = Post.objects.filter(category = post.category).exclude(pk=post.id)

  except Post.DoesNotExist:
    raise Http404("The Post Doesn't Exist")
  
  return render(request, 'detail.html', {'post': post, 'related_posts':related_posts})

def payment(request):
  return HttpResponse("You are currently in the payment page")

def delivery(request, place_id):
  return HttpResponse(f"You are at delivery place: {place_id}")

def old_url_redirect(request):
  return redirect(reverse("blog:new_url"))

def new_url_view(request):
  return HttpResponse("this is the new url")

def contact_view(request):
    if request.method == 'POST':
      form = ContactForm(request.POST) # retrieves the data entered in the fields of the contact form
      name = request.POST.get('name')
      email = request.POST.get('email')
      message = request.POST.get('message')

      if form.is_valid() :
        logger = logging.getLogger("TESTING")
        logger.debug(f"POST Data is {form.cleaned_data['name']}, {form.cleaned_data['email']}, {form.cleaned_data['message']}")
        success_message = "Your form has been submitted!"
        return render(request, 'contact.html', {'form':form, 'success_message':success_message})  
      else:
        logger.debug("Form validation failed!")
      return render(request, 'contact.html', {'form':form, 'name':name, 'email':email, 'message':message})  
    return render(request, 'contact.html')  

def about_view(request):
  about_us_content = AboutUs.objects.first()
  if about_us_content is None or not about_us_content:
    about_us_content.content = "This is the about page content"
  return render(request, 'about.html', {'about_us_content':about_us_content})