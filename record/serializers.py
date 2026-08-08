from rest_framework import serializers
from.models import Students,Course,Enrollment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
      model = Course
      fields = "__all__"


class EnrollmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"

        


