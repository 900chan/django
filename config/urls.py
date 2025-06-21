from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/feeds/", include("feeds.urls")),
    # path("api/v1/users", include("users.urls")),
    # path("api/v1/reviews", include("reviews.urls")),
#     path("feeds/", views.show_feed),
#     path("feeds/all", views.all_feed),
#     path("feeds/<int:feed_id>/<str:feed_content>", views.one_feed),
]
