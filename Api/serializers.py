from rest_framework import serializers
from .models import create_blog

# Create your serializers here.

class BlogSerializer(serializers.ModelSerializer):
    """
    Serializer for the create_blog model with all fields
    """
    class Meta:
        model = create_blog
        fields = '__all__'
        read_only_fields = ('date',)
    
    def validate_title(self, value):
        """
        Check that the title is not empty and has reasonable length
        """
        if len(value.strip()) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        return value
    
    def validate_content(self, value):
        """
        Check that the content is not empty
        """
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Content must be at least 10 characters long.")
        return value


class BlogListSerializer(serializers.ModelSerializer):
    """
    Simplified serializer for listing blogs (without full content)
    """
    content_preview = serializers.SerializerMethodField()
    
    class Meta:
        model = create_blog
        fields = ['id', 'title', 'slug', 'Author_name', 'date', 'image', 'Category', 'content_preview']
    
    def get_content_preview(self, obj):
        """
        Return first 200 characters of content as preview
        """
        return obj.content[:200] + '...' if len(obj.content) > 200 else obj.content


class BlogCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating new blog posts
    """
    class Meta:
        model = create_blog
        fields = ['title', 'slug', 'Author_name', 'content', 'image', 'Category']
    
    def validate_slug(self, value):
        """
        Check that the slug is unique
        """
        if create_blog.objects.filter(slug=value).exists():
            raise serializers.ValidationError("A blog with this slug already exists.")
        return value


class BlogUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating existing blog posts
    """
    class Meta:
        model = create_blog
        fields = ['title', 'slug', 'Author_name', 'content', 'image', 'Category']
    
    def validate_slug(self, value):
        """
        Check that the slug is unique (excluding current instance)
        """
        instance = self.instance
        if instance and create_blog.objects.filter(slug=value).exclude(pk=instance.pk).exists():
            raise serializers.ValidationError("A blog with this slug already exists.")
        return value