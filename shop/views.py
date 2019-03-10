from django.views.generic import ListView
from . import models


class BookListView(ListView):
    model = models.Book
    paginate_by = 5

