
from django.urls import path
from . import views

# API URL patterns for blog application
urlpatterns = [
    # Blog CRUD operations
    path('blogs/', views.BlogListCreateView.as_view(), name='blog-list-create'),
    path('blogs/<str:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),
    
    # Blog by slug
    path('blogs/slug/<slug:slug>/', views.BlogBySlugView.as_view(), name='blog-by-slug'),
    
    # Blog by category
    path('blogs/category/<str:category>/', views.BlogByCategoryView.as_view(), name='blog-by-category'),
    
    # Blog search
    path('blogs/search/', views.BlogSearchView.as_view(), name='blog-search'),
    
    # Recent blogs
    path('blogs/recent/', views.RecentBlogsView.as_view(), name='recent-blogs'),
    
    # Utility endpoints
    path('categories/', views.blog_categories, name='blog-categories'),
    path('stats/', views.blog_stats, name='blog-stats'),
]
