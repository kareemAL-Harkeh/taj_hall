from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.views.generic import ListView , DetailView
from django.views.generic.edit import UpdateView , DeleteView ,CreateView
from .models import Book
from django.views import View
from .forms import BookForm
import datetime

from django.views.generic import TemplateView

class HomePageView(LoginRequiredMixin, ListView) :

    model= Book
    template_name ="index.html"
    login_url= 'login'
    


class BookCreateView(LoginRequiredMixin, CreateView, View):
    
    model = Book
    template_name = 'book.html'
    form_class= BookForm
    login_url = 'login'

    def form_valid(self, form_class):
        form_class.instance.author = self.request.user
        return super().form_valid(form_class)

    def post(self, request, *args, **kwargs) -> HttpResponse:
        if  Book.objects.filter(tim= request.POST['tim']).count() != 0 and Book.objects.filter(dat= request.POST['dat']).count() != 0 :
            books= Book.objects.filter(dat= request.POST['dat'])
            context= {'books': books}
            return render(request, 'error.html', context)
        elif Book.objects.filter(dat= request.POST['dat']).count() != 0 :
            for i in Book.objects.filter(dat= request.POST['dat']) :
                if int(request.POST['tim'][:2]) in range(i.tim.hour,(i.tim.hour+ int(i.num_of_hour))):
                    books= Book.objects.filter(dat= request.POST['dat'])
                    context= {'books': books}
                    return render(request, 'error.html', context)
                else:
                    return super().post(request)
        elif int(datetime.datetime.now().year) >= int(request.POST['dat'][:4]) and int(datetime.datetime.now().month) >= int(request.POST['dat'][8:]) and int(datetime.datetime.now().day) >= int(request.POST['dat'][5:7]) :
            return HttpResponse('تاريخ قديم')
        else:
            return super().post(request)
                

class BookListView(ListView,LoginRequiredMixin):
    model= Book
    template_name= 'my_books.html'
    login_url= 'login'
    

class DonePageView(TemplateView) :
    
    template_name ="done.html"

class BookRequestsListView(ListView,LoginRequiredMixin,UserPassesTestMixin):
    model= Book
    template_name= 'books_requests.html'
    login_url= 'login'
    
    def test_func(self) -> bool | None:
        
        return self.request.user.is_staff == True

class BookUpdateView(LoginRequiredMixin ,UserPassesTestMixin ,UpdateView) :

    model = Book
    fields = ('name', 'accsepted', 'reson', )
    template_name = 'book_edit.html'
    login_url = 'login'
    def test_func(self) -> bool | None:
        
        return self.request.user.is_staff == True

class BookDetailView(LoginRequiredMixin, DetailView) :

    model = Book
    template_name = 'book_detail.html'
    login_url = 'login'
    
    
class BookDeleteView(LoginRequiredMixin,UserPassesTestMixin , DeleteView): # new

    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('books_requests')
    login_url = 'login'

    def test_func(self) -> bool | None:
        
        return self.request.user.is_staff == True
