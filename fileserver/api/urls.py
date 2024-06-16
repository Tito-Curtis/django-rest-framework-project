from files.views import (DeleteRetrieveUpdate, index,person,post_id,
                        ApiViewExample,PostViewSet)
from django.urls import path


urlpatterns = [
    path('', index,name="home"),
    path('person/',person,name="person"),
    path('api_eg/',ApiViewExample.as_view(),name="api_example"),
    path('post/<int:post_id>',post_id,name="post_id"),
    path('viewset/',PostViewSet.as_view(),name="using_viewset"),
    path('view/<int:pk>/',DeleteRetrieveUpdate.as_view(),)

]