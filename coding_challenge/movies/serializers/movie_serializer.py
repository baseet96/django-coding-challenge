from coding_challenge.movies.serializers.review_serializer import ReviewSerializer
from rest_framework import serializers

from movies.models import Movie

class RuntimeFormattedField(serializers.Field):
    def to_representation(self, value):
        hours = value // 60
        minutes = value % 60
        return f"{hours}:{minutes:02d}"

class MovieSerializer(serializers.ModelSerializer):

    runtime_formatted = RuntimeFormattedField(source='runtime')
    reviews = ReviewSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()
    
    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "runtime",
            "runtime_formatted",
            "release_date",
            "reviews",
            "avg_rating"
        )
        
    def get_avg_rating(self, obj):
        reviews = obj.reviews.all()
        if not reviews:
            return None
        avg = sum(review.rating for review in reviews) / reviews.count()
        return round(avg, 2)