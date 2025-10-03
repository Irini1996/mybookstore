from django.contrib import admin
from .models import Book 

class BookAdmin(admin.ModelAdmin): #Create a custom configuration class for how the Book model will behave in the admin.
#It inherits from admin.ModelAdmin, which is the base class with lots of options.

  
    list_display = ("title", "author", "price", "created_at") #Controls which columns are shown in the list view of books.
#Instead of only seeing the __str__ value (the title), you’ll see columns for title, author, price, and created date.

    search_fields = ("title", "author") #Adds a search box at the top of the book list.

   
    list_filter = ("author",)

    ordering = ("title",)

    date_hierarchy = "created_at" #Adds a date-based navigation bar above the book list.

    list_display_links = ("title",) #It just makes the title clickable.

admin.site.register(Book, BookAdmin) #Registers the Book model with the admin site using the BookAdmin configuration.


admin.site.site_header = "MyBookstore Admin"
admin.site.site_title = "MyBookstore"
admin.site.index_title = "Site administration"


