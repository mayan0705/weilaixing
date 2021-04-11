from rest_framework import serializers
from .models import Administrator
from .models import Camp
from .models import Campclass
from .models import Course
from .models import Coursebystander
from .models import User
from .models import Campsignup
from .models import Campattend
from .models import Userdata
from .models import Usercompany
from .models import Activity
from .models import Activitytakes
from .models import Coursefile


class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = ('admin_name', 'admin_password', 'power_create_camp',
                  'power_create_course', 'power_create_activity', 'power_create_administrator')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'time', 'location', 'teacher', 'abstract', 'belongto_camp',
                  'belongto_campclass', 'number_bystander', 'bystand_tips')


class CampclassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campclass
        fields = ('id', 'name', 'student_number', 'camp_id')


class CampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camp
        fields = ('id', 'name', 'time', 'introduce', 'people_oriented',
                  'signin_tips', 'signin_deadline', 'permission')


class CoursebystanderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coursebystander
        fields = ('id', 'user_id', 'course_id')


class CampsignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campsignup
        fields = ('id', 'user_id', 'camp_id', 'campclass_id')


class CampattendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campattend
        fields = ('id', 'user_id', 'camp_id')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'user_name', 'user_gender', 'user_weixinnumber',
                  'user_telephone', 'user_email')


class UserdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userdata
        fields = ('id', 'user_id', 'user_birthday', 'user_company', 'user_post', 'user_city', 'user_referee1_message', 'user_referee2_message', 'user_referee3_message', 'user_other_tips_message_question_for_absenceitem',
                  'reasons_for_signin', 'contribution_to_others', 'messageway_to_camp', 'educated_condition', 'user_educondition_time_detials', 'user_beforestartup_company_condition')


class UsercompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Usercompany
        fields = ('id', 'name', 'brand_name', 'website', 'app_or_publicAccounts', 'startup_time', 'center_city', 'membership',
                  'abstract', 'main_operational_data', 'income_scale', 'financing_situation', 'value_of_assessment', 'additions')


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'activity_name', 'activity_time', 'activity_location', 'activity_abstract',
                  'activity_peopleneed', 'activity_tips', 'activity_status', 'activity_items')


class ActivitytakesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activitytakes
        fields = ('id', 'attender_id', 'activity_id')


class CoursefileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coursefile
        fields = ('id', 'course_id', 'ppt_name', 'ppt', 'video_name',
                  'video', 'text_name', 'text', 'others_name', 'others')
