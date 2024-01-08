from rest_framework import serializers
from .models import PostModel,CommentModel

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = "__all__"

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ('id', 'author')

class CommentSerializer(serializers.ModelSerializer):
   # post = PostSerializer()
    post = serializers.PrimaryKeyRelatedField(queryset=PostModel.objects.all())
    

    class Meta:
        model = CommentModel
        fields = "__all__"
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        post_id = representation['post']
        try:
            post = PostModel.objects.get(pk=post_id)
            post_data = PostCommentSerializer(post).data  # Serialize the related post using the subset serializer
            representation['post'] = post_data  # Update 'post' field with custom representation
        except PostModel.DoesNotExist:
            pass  # Handle the case when the related post doesn't exist
        return representation