from django.contrib import admin
from .models import Room, Booking, ChatMessage, UserProfile

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'room_type', 'price']  # remove invalid ones
    ordering = ['id']
    search_fields = ['room_type']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'room', 'check_in', 'check_out']
    search_fields = ['user_username', 'room_room_type']


from django.contrib import admin
from .models import ChatRoom, ChatMessage

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_group', 'created_at')
    filter_horizontal = ('members',)

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'room', 'timestamp', 'is_delivered', 'is_read')
    list_filter = ('timestamp', 'room', 'sender', 'is_read', 'is_delivered')
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'gender', 'joined')
    search_fields = ('user__username', 'phone_number')
    list_filter = ('gender',)
    ordering = ('-joined',)
# main/admin.py

from django.contrib import admin
from .models import Room, Booking, ChatMessage, Payment, Resource, Entertainment

@admin.register(Entertainment)
class EntertainmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_added')
    list_filter = ('category', 'date_added')
    search_fields = ('title', 'description')
    ordering = ('-date_added',)
from django.contrib import admin
from .models import Resource

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_by', 'uploaded_at')
    search_fields = ('title', 'description')
    list_filter = ('uploaded_at',)

