
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet,CourseViewSet,EnrollmentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'course', CourseViewSet)
router.register(r'enrollment', EnrollmentViewSet)



urlpatterns = [
    path('', include(router.urls)),
]
