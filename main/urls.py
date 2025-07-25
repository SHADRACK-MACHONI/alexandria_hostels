from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('rooms/', views.rooms_view, name='rooms'),
    path('book-room/<int:room_id>/', views.book_room, name='book_room'),
    path('payments/', views.payments_view, name='payments'),  # define this
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('resources/', views.resource_list, name = 'resources'),
    path('chat/', views.chat_view, name='chat'),  # Add this
    path('entertainment/', views.entertainment_view, name = 'entertainment'),
]


