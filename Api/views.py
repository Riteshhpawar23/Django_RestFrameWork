from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import create_blog
from .serializers import (
    BlogSerializer, 
    BlogListSerializer, 
    BlogCreateSerializer, 
    BlogUpdateSerializer
)

# Create your views here.

class BlogPagination(PageNumberPagination):
    """
    Custom pagination for blog posts
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


class BlogListCreateView(generics.ListCreateAPIView):
    """
    List all blogs or create a new blog
    GET: Returns paginated list of all blogs
    POST: Creates a new blog post
    """
    queryset = create_blog.objects.all().order_by('-date')
    pagination_class = BlogPagination
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BlogCreateSerializer
        return BlogListSerializer
    
    def get_queryset(self):
        queryset = create_blog.objects.all().order_by('-date')
        
        # Filter by category
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(Category__icontains=category)
        
        # Search in title and content
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | 
                Q(content__icontains=search) |
                Q(Author_name__icontains=search)
            )
        
        return queryset


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a blog post
    GET: Returns detailed blog post
    PUT/PATCH: Updates blog post
    DELETE: Deletes blog post
    """
    queryset = create_blog.objects.all()
    
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return BlogUpdateSerializer
        return BlogSerializer
    
    def get_object(self):
        """
        Allow retrieval by either ID or slug
        """
        lookup_value = self.kwargs.get('pk')
        
        # Try to get by ID first, then by slug
        try:
            # If lookup_value is a number, get by ID
            int(lookup_value)
            return get_object_or_404(create_blog, pk=lookup_value)
        except ValueError:
            # If not a number, get by slug
            return get_object_or_404(create_blog, slug=lookup_value)


class BlogBySlugView(generics.RetrieveAPIView):
    """
    Retrieve a blog post by slug
    """
    serializer_class = BlogSerializer
    lookup_field = 'slug'
    queryset = create_blog.objects.all()


class BlogByCategoryView(generics.ListAPIView):
    """
    List blogs filtered by category
    """
    serializer_class = BlogListSerializer
    pagination_class = BlogPagination
    
    def get_queryset(self):
        category = self.kwargs.get('category')
        return create_blog.objects.filter(Category__iexact=category).order_by('-date')


class BlogSearchView(generics.ListAPIView):
    """
    Search blogs by title, content, or author
    """
    serializer_class = BlogListSerializer
    pagination_class = BlogPagination
    
    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        if query:
            return create_blog.objects.filter(
                Q(title__icontains=query) | 
                Q(content__icontains=query) |
                Q(Author_name__icontains=query)
            ).order_by('-date')
        return create_blog.objects.none()


@api_view(['GET'])
def blog_categories(request):
    """
    Get all available blog categories
    """
    categories = [choice[0] for choice in create_blog.typeofblog]
    return Response({
        'categories': categories,
        'count': len(categories)
    })


@api_view(['GET'])
def blog_stats(request):
    """
    Get blog statistics
    """
    total_blogs = create_blog.objects.count()
    categories_count = {}
    
    for category_key, category_display in create_blog.typeofblog:
        count = create_blog.objects.filter(Category=category_key).count()
        categories_count[category_key] = {
            'display_name': category_display,
            'count': count
        }
    
    return Response({
        'total_blogs': total_blogs,
        'categories': categories_count
    })


class RecentBlogsView(generics.ListAPIView):
    """
    Get recent blog posts (latest 5)
    """
    serializer_class = BlogListSerializer
    
    def get_queryset(self):
        limit = self.request.query_params.get('limit', 5)
        try:
            limit = int(limit)
        except ValueError:
            limit = 5
        
        return create_blog.objects.all().order_by('-date')[:limit]