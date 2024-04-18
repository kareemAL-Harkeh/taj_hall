from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name= 'home'),
    path('book', views.BookCreateView.as_view(), name= 'book'),
    path('messgae', views.DonePageView.as_view(), name= 'done'),
    path('my_books', views.BookListView.as_view(), name= 'my_books'),
    path('books_requests',views.BookRequestsListView.as_view(), name= 'books_requests'),
    path('<int:pk>/edit',views.BookUpdateView.as_view(), name='book_edit'),
    path('<int:pk>/',views.BookDetailView.as_view(), name='book_detail'),
    path('<int:pk>/delete/',views.BookDeleteView.as_view(), name='article_delete'),
    
]
