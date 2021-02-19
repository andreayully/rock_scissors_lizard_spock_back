from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from gameElements.views import GameElementListView, InitialMatchCreateView, MatchRetriveUpdateView

urlpatterns = {
    path('elements/', GameElementListView.as_view(), name="list-elements"),
    path('initial-match/', InitialMatchCreateView.as_view(), name="initial-match"),
    path('match/<str:pk>/', MatchRetriveUpdateView.as_view(), name="retrive-update-match"),

}
urlpatterns = format_suffix_patterns(urlpatterns)
