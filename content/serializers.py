from rest_framework.serializers import ModelSerializer
from .models import UserPost, PostMedia, PostLikes, PostComments
from api.serializers import UserProfileViewSerializer


class UserPostCreateSerializer(ModelSerializer):

    def create(self, validated_data):
        validated_data['author'] = self.context['current_user']
        return UserPost.objects.create(**validated_data)

    class Meta:
        model = UserPost
        fields = ['caption_text', 'location', 'id', 'is_published']


class PostMediaCreateSerializer(ModelSerializer):
    class Meta:
        model = PostMedia
        fields = ['media_file', 'sequence_index', 'post']


class PostMediaViewSerializer(ModelSerializer):
    class Meta:
        model = PostMedia
        exclude = ['post', ]


class PostFeedSerializer(ModelSerializer):
    # TODO:: Create a serializer with more proper representation of author in Feed

    author = UserProfileViewSerializer()
    media = PostMediaViewSerializer(many=True)

    class Meta:
        model = UserPost
        fields = '__all__'
        include = ('media',)


class PostLikeSerializer(ModelSerializer):
    def create(self, validated_data):
        validated_data['liked_by'] = self.context['current_user']
        return PostLikes.objects.create(**validated_data)

    class Meta:
        model = PostLikes
        fields = ('id', 'post')


class PostCommentSerializer(ModelSerializer):
    def create(self, validated_data):
        validated_data['author'] = self.context['current_user']
        return PostComments.objects.create(**validated_data)

    class Meta:
        model = PostComments
        fields = ('id', 'post', 'text')
