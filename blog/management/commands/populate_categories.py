from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand

class Command(BaseCommand):
  help = "This command inserts category data"

  def handle(self, *args: Any, **options: Any):
    # Delete existing data 
    Category.objects.all().delete()
   
    categories = [
        "Technology",
        "Health",
        "Productivity & Lifestyle",
        "Travel & Exploration",
        "Hobbies & Personal Development",
        "Sustainability & Environment",
        "Personal Growth & Branding",
        "Gadgets & Tools"
    ]

    for category_name in categories:
      Category.objects.create(name=category_name)

    self.stdout.write(self.style.SUCCESS("Completed Inserting data"))

