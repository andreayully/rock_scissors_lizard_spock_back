from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from users.views import UserCreateListView

urlpatterns = {
    path('', UserCreateListView.as_view(), name="create-list"),
}
urlpatterns = format_suffix_patterns(urlpatterns)
