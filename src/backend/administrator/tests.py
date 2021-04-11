from django.test import TestCase
from django.test.utils import setup_test_environment
from django.test import Client
import json
from .models import Administrator
from .models import Camp
from .models import Campclass
from .models import Course
from .models import Coursebystander
from .models import Campattend
from .models import Campsignup
from .models import User
from .models import Userdata
from .models import Usercompany
from .models import Activity
from .models import Activitytakes
from .models import Coursefile
from .serializers import AdministratorSerializer
from .serializers import CampSerializer
from .serializers import CampclassSerializer
from .serializers import CourseSerializer
from .serializers import CoursebystanderSerializer
from .serializers import CampsignupSerializer
from .serializers import CampattendSerializer
from .serializers import UserSerializer
from .serializers import UserdataSerializer
from .serializers import UsercompanySerializer
from .serializers import ActivitySerializer
from .serializers import ActivitytakesSerializer
from .serializers import CoursefileSerializer
from .views import adminForLogin
from .views import ifSignupCamp
from .views import signupCamp
from .views import createActivity
from .views import modifyActivity
from .views import addAdministrator
from .views import courseinCamp
from .views import schoolmateData
from .views import getPreviousCampMessage
from .views import ifinActivity
from .views import attendActivity
from .views import createNewCamp
from .views import selectSchoolmate
from .views import queryAdministrator
from .views import modifyAdministrator
from .views import alterUserData
from .views import weixinLogin
from .views import weixinRegister
from .views import initializeData
from .views import changeTelephone
from .views import querySchoolmate
from .views import selectSpecificSchoolmate
from .views import queryCampSignup
from .views import queryCamps
from .views import specificCampMsg
from .views import modifyCampMsg
from .views import queryActivity
from .views import specificActivityMsg
from .views import getId
from .views import weixinAddUser
# Create your tests here.


class ActivitytakesTestCase(TestCase):
    def setUp(self):
        Activitytakes.objects.create(attender_id=1, activity_id=2)

    def test_activitytakes(self):
        Ldy = Activitytakes.objects.get(attender_id=1)
        self.assertEqual(Ldy.activity_id, 2)


class CampclassTestCase(TestCase):
    def setUp(self):
        Campclass.objects.create(name='123', student_number=10, camp_id=6)

    def test_campclass(self):
        la = Campclass.objects.get(name='123')
        self.assertEqual(la.student_number, 10)


class AdministratorTestCase(TestCase):
    def setUp(self):
        Administrator.objects.create(admin_name='hhhh', admin_password='1232', power_create_camp=False,
                                     power_create_course=False, power_create_activity=False, power_create_administrator=False)

    def test_administrator(self):
        ldy = Administrator.objects.get(admin_name='hhhh')
        self.assertEqual(ldy.admin_password, '1232')


class CampTestCase(TestCase):
    def setUp(self):
        Camp.objects.create(name='lmjnb', time='lmjnb', introduce='introduce',
                            people_oriented='people_oriented', signin_tips='signin_tips', signin_deadline='signin_deadline')

    def test_camp(self):
        camp = Camp.objects.get(name='lmjnb')
        self.assertEqual(camp.introduce, 'introduce')


class CourseTestCase(TestCase):
    def setUp(self):
        Course.objects.create(name='name', time='time', location='location', teacher='teacher', abstract='abstract',
                              belongto_camp='belongto_camp', belongto_campclass='belongto_campclass', number_bystander=12, bystand_tips='bystand_tips')

    def test_course(self):
        course = Course.objects.get(name='name')
        self.assertEqual(course.time, 'time')


class CoursebystanderTestCase(TestCase):
    def setUp(self):
        Coursebystander.objects.create(user_id=1, course_id=12)

    def test_coursebystander(self):
        coursebystander = Coursebystander.objects.get(user_id=1)
        self.assertEqual(coursebystander.course_id, 12)


class CampsignupTestCase(TestCase):
    def setUp(self):
        Campsignup.objects.create(user_id=12, camp_id=15)

    def test_campsignup(self):
        campsignup = Campsignup.objects.get(user_id=12)
        self.assertEqual(campsignup.camp_id, 15)


class CampattendTestCase(TestCase):
    def setUp(self):
        Campattend.objects.create(user_id=1, camp_id=2)

    def test_campattend(self):
        campattend = Campattend.objects.get(user_id=1)
        self.assertEqual(campattend.camp_id, 2)


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(user_name='user', user_gender='m', user_weixinnumber='weixinnumber',
                            user_telephone='15522055116', user_email='1152487659@qq.com')

    def test_user(self):
        user = User.objects.get(user_name='user')
        self.assertEqual(user.user_email, '1152487659@qq.com')
        self.assertEqual(user.get_user_gender_display(), '男')


class UserdataTestCase(TestCase):
    def setUp(self):
        Userdata.objects.create(user_id=1, user_birthday='2019/8/6', user_company='12', user_post='F', user_city='北京', user_referee1_message='lllasdad', user_referee2_message='lllasdad', user_referee3_message='lllasdad',
                                user_other_tips_message_question_for_absenceitem='认可', reasons_for_signin='ladd', contribution_to_others='jsdkahk', messageway_to_camp='weixin', educated_condition='PhD', user_educondition_time_detials='asdasd', user_beforestartup_company_condition='164')

    def test_userdata(self):
        userdata = Userdata.objects.get(user_id=1)
        self.assertEqual(userdata.get_user_post_display(), '创始人')
        self.assertEqual(userdata.get_messageway_to_camp_display(), '微信朋友圈')
        self.assertEqual(userdata.get_educated_condition_display(), '博士研究生')


class UsercompanyTestCase(TestCase):
    def setUp(self):
        Usercompany.objects.create(name='llll', brand_name='467', website='565', app_or_publicAccounts='46', startup_time='2019/8/6', center_city='北京', membership=10000,
                                   abstract='1165', main_operational_data='446466', income_scale='164', financing_situation='N', value_of_assessment='1655000', additions='164')

    def test_usercompny(self):
        usercompany = Usercompany.objects.get(brand_name='467')
        self.assertEqual(usercompany.website, '565')
        self.assertEqual(
            usercompany.get_financing_situation_display(), '尚未获得融资')


class ActivityTestCase(TestCase):
    def setUp(self):
        Activity.objects.create(activity_name='lmjnb', activity_time='2019/8/6', activity_location='泰达学院5区',
                                activity_abstract='135', activity_peopleneed=12, activity_tips='1564', activity_status='N', activity_items='456')

    def test_activity(self):
        activity = Activity.objects.get(activity_name='lmjnb')
        self.assertEqual(activity.activity_time, '2019/8/6')
        self.assertEqual(activity.get_activity_status_display(), 'NotStart')


class RecommandTestCase(TestCase):
    def setUp(self):
        Coursefile.objects.create(Coursefileer_name='1232', Coursefileer_companyandpost='154', Coursefileer_telephone='15522055116',
                                  Coursefileed_name='1654', Coursefileed_company='13', Coursefileed_class='nasda', Coursefileer_reasons='55')

    def test_Coursefile(self):
        Coursefile = Coursefile.objects.get(Coursefileer_name='1232')
        self.assertEqual(Coursefile.Coursefileer_telephone, '15522055116')


class def_adminForLogin(TestCase):  # 1
    def test_adminForLogin(self):
        obj = Administrator.objects.create(admin_name='admin', admin_password='admin', power_create_camp=False,
                                           power_create_course=False, power_create_activity=False, power_create_administrator=False)
        response = self.client.post(
            '/adminForLogin/', {'admin_name': 'admin', 'admin_password': 'admin'})
        self.assertEqual(json.loads(response.content)['code'], 'ok')


class def_ifSignupCamp(TestCase):
    def test_ifSignupCamp(self):
        obj = Campsignup.objects.create(user_id=1, camp_id=1)
        response = self.client.get(
            '/ifSignupCamp/', {'user_id': 1, 'camp_id': 1})
        self.assertEqual(json.loads(response.content)['statuscode'], '200')

# class def_signupCamp(TestCase): # 3


class def_createActivity(TestCase):
    def test_createActivity(self):
        response = self.client.post('/creareActivity/',
                                    {'activity_name': 'hello',
                                        'activity_time': '2019-05-07 11:00:00;2019-05-07 13:00:00',
                                        'activity_location': '泰达校区五阶',
                                        'activity_abstract': 'sadasknd',
                                        'activity_peopleneed': 20,
                                        'activity_tips': 'asdas',
                                        'activity_status': 'N'})
        self.assertEqual(json.loads(response.content)['code'], '1')


class def_addAdministrator(TestCase):
    def test_addAdministrator(self):
        response = self.client.post('/addAdministrator/', {'admin_name': 'admin', 'admin_password': 'admin', 'power_create_camp': False,
                                                           'power_create_course': False, 'power_create_activity': False, 'power_create_administrator': False})
        self.assertEqual(json.loads(response.content)['code'], '1')

# class def_courseinCamp(TestCase): # 6

# class def_schoolmateData(TestCase): # 7

# class def_modifyActivity(TestCase): # 8

# class def_getPreviousCampMessage(TestCase): # 9

# class def_ifinActivity(TestCase): # 10

# class def_attendActivity(TestCase): # 11


class def_createNewCamp(TestCase):
    def test_createNewCamp(self):
        response = self.client.post('/createNewCamp/', {
            'name': '新的创业营',
            'time': '2019-12-15,2020-01-11',
            'introduce': 'hhhh',
            'people_oriented': '中二少年',
            'signin_tips': 'must be zhonger younger',
            'signin_deadline': '2019-11-05'})
        self.assertEqual(json.loads(response.content)['code'], '1')

# class def_selectSchoolmate(TestCase): # 13

# class def_queryAdministrator(TestCase): # 14

# class def_modifyAdministrator(TestCase): # 15

# class def_alterUserData(TestCase): # 16

# class def_weixinLogin(TestCase): # 17

# class def_weixinRegister(TestCase): # 18

# class def_initializeData(TestCase): # 19

# class def_changeTelephone(TestCase): # 20

# class def_querySchoolmate(TestCase): # 21

# class def_selectSpecificSchoolmate(TestCase): # 22

# class def_queryCampSignup(TestCase): # 23

# class def_queryCamps(TestCase): # 24

# class def_specificCampMsg(TestCase): # 25


class def_modifyCampMsg(TestCase):  # 26
    def test_modifyCampMsg(self):
        response = self.client.post('/modifyCampMsg/', {'id': '25', 'name': '第一期创新院', 'time': '2019-08-01,2019-08-07',
                                                        'introduce': '欢迎来到王者荣耀', 'people_oriented': '各年龄段王者荣耀人群', 'signin_tips': '须达到王者段位', 'signin_deadline': '2019-08-07'})
        self.assertEqual(json.loads(response.content)['code'], '1')


# class def_queryActivity(TestCase): # 27

# class def_specificActivityMsg(TestCase): # 28

# class def_weixinAddUser(TestCase): #29

# class def_getId(TestCase): #30
