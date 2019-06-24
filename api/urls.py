from django.urls import path, include

from .views import TodoListCreateAPIView, TodoRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('<int:pk>', TodoRetrieveUpdateDestroyAPIView.as_view()),
    path('', TodoListCreateAPIView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]