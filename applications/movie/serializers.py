from django.db.models import Avg
from rest_framework import serializers

from applications.movie.models import *


class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField()

    class Meta:
        model = Review
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField()
    comments = ReviewSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        files_data = request.FILES
        movie = Movie.objects.create(**validated_data)

        for image in files_data.getlist('images'):
            Image.objects.create(movie=movie, image=image)
        return movie

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['likes'] = instance.likes.filter(like=True).count()  # кол-во лайков
        rep['rating'] = instance.ratings.all().aggregate(Avg('rating'))['rating__avg']  # сред рейтинга
        return rep


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Rating
        fields = ['rating']
