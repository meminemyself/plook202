from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Tree, PlantingLocation, UserPlanting, Notification, Equipment, NewsArticle, Purchase



@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
@admin.register(PlantingLocation)
class PlantingLocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location_type')
    search_fields = ('name', 'location_type')
    list_filter = ('location_type',)

@admin.register(UserPlanting)
class UserPlantingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'tree', 'location', 'planting_date', 'is_completed')
    search_fields = ('user__username', 'tree__name', 'location__name')
    list_filter = ('is_completed', 'planting_date')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'message', 'notification_date', 'is_read')
    search_fields = ('user__username', 'message')
    list_filter = ('is_read',)

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'equipment', 'quantity', 'purchase_date')
    search_fields = ('user__username', 'equipment__name')
    list_filter = ('purchase_date',)

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)