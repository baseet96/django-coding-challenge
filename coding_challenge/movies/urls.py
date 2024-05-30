from django.urls import path

from movies.views import MovieListView, MovieDetail

urlpatterns = [
    path("", MovieListView.as_view(), name="MovieListView"),
    path('<int:pk>/', MovieDetail.as_view(), name='MovieDetail'),
]