from typing import Any
from blog.models import Post, Category
from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
  help = "This command inserts post data"

  def handle(self, *args: Any, **options: Any):
    # Delete existing data 
    Post.objects.all().delete()
    titles = [
        "10 Tips for Effective Remote Work",
        "Exploring the Hidden Gems of Europe",
        "Mastering Python for Data Science",
        "The Ultimate Guide to Healthy Eating",
        "Top 5 Gadgets You Can't Live Without",
        "How to Boost Your Productivity at Work",
        "The Art of Minimalist Living",
        "Photography Hacks for Beginners",
        "Understanding Blockchain Technology",
        "The Rise of AI in Everyday Life",
        "How to Travel on a Budget",
        "The Science Behind Better Sleep",
        "Gardening for Small Spaces",
        "The Future of Renewable Energy",
        "Building a Personal Brand Online",
        "Tips for Writing Engaging Blog Posts",
        "How to Stay Fit While Working from Home",
        "The Importance of Mental Health Awareness",
        "Learning a New Language as an Adult",
        "The Pros and Cons of Electric Vehicles"
    ]

    contents = [
        "Remote work has become the norm, but staying productive at home can be a challenge. These 10 tips will help you thrive.",
        "Europe is full of hidden treasures beyond the usual tourist spots. Discover these underrated destinations.",
        "Python is a powerful tool for data science. Learn the key libraries and techniques to master it.",
        "Healthy eating doesn't have to be complicated. Follow this guide to create a balanced diet.",
        "From smartwatches to noise-canceling headphones, these gadgets make life easier and more fun.",
        "Struggling with distractions? Here are proven strategies to help you get more done in less time.",
        "Minimalism isn't just a trend; it's a way to simplify your life. Learn how to embrace it.",
        "Photography can be intimidating for beginners. These hacks will make it easy to capture stunning photos.",
        "Blockchain is more than just cryptocurrency. Discover how it's transforming various industries.",
        "AI is no longer a futuristic concept. See how it's already influencing our daily routines.",
        "Traveling doesn't have to break the bank. Learn how to explore the world on a budget.",
        "Sleep is crucial for health and productivity. Discover the science behind getting better rest.",
        "No backyard? No problem! These gardening tips are perfect for small spaces or urban living.",
        "Renewable energy is the future. Explore the latest innovations shaping a sustainable world.",
        "Your online presence matters. Learn how to build a strong personal brand in the digital age.",
        "Want to keep readers hooked? Use these tips to write blog posts that people love to read.",
        "Fitness routines can be tricky when you're home all day. Stay active with these simple exercises.",
        "Mental health is just as important as physical health. Learn how to prioritize it in your daily life.",
        "Learning a language isn't just for kids. Here are strategies to make it easier for adults.",
        "Electric vehicles are the talk of the town. Explore the benefits and challenges they bring."
    ]

    image_urls = [
        "https://picsum.photos/id/1/800/400",
        "https://picsum.photos/id/2/800/400",
        "https://picsum.photos/id/3/800/400",
        "https://picsum.photos/id/4/800/400",
        "https://picsum.photos/id/5/800/400",
        "https://picsum.photos/id/6/800/400",
        "https://picsum.photos/id/7/800/400",
        "https://picsum.photos/id/8/800/400",
        "https://picsum.photos/id/9/800/400",
        "https://picsum.photos/id/10/800/400",
        "https://picsum.photos/id/11/800/400",
        "https://picsum.photos/id/12/800/400",
        "https://picsum.photos/id/13/800/400",
        "https://picsum.photos/id/14/800/400",
        "https://picsum.photos/id/15/800/400",
        "https://picsum.photos/id/16/800/400",
        "https://picsum.photos/id/17/800/400",
        "https://picsum.photos/id/18/800/400",
        "https://picsum.photos/id/19/800/400",
        "https://picsum.photos/id/20/800/400"
    ]

    categories = Category.objects.all()
    for title, content, image_url in zip(titles, contents, image_urls):
      category = random.choice(categories)
      Post.objects.create(title=title, content=content, img_url=image_url, category=category)

    self.stdout.write(self.style.SUCCESS("Completed Inserting data"))

