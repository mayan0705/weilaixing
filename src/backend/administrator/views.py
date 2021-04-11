from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.core import serializers
from rest_framework import viewsets
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
from yunpian_python_sdk.model import constant as YC
from yunpian_python_sdk.ypclient import YunpianClient
import random
# Create your views here.


class AdministratorView(viewsets.ModelViewSet):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer


class CampView(viewsets.ModelViewSet):
    queryset = Camp.objects.all()
    serializer_class = CampSerializer


class CampclassView(viewsets.ModelViewSet):
    queryset = Campclass.objects.all()
    serializer_class = CampclassSerializer


class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CoursebystanderView(viewsets.ModelViewSet):
    queryset = Coursebystander.objects.all()
    serializer_class = CoursebystanderSerializer


class CampsignupView(viewsets.ModelViewSet):
    queryset = Campsignup.objects.all()
    serializer_class = CampsignupSerializer


class CampattendView(viewsets.ModelViewSet):
    queryset = Campattend.objects.all()
    serializer_class = CampattendSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserdataView(viewsets.ModelViewSet):
    queryset = Userdata.objects.all()
    serializer_class = UserdataSerializer


class UsercompanyView(viewsets.ModelViewSet):
    queryset = Usercompany.objects.all()
    serializer_class = UsercompanySerializer


class ActivityView(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class ActivitytakesView(viewsets.ModelViewSet):
    queryset = Activitytakes.objects.all()
    serializer_class = ActivitytakesSerializer


class CoursefileView(viewsets.ModelViewSet):
    queryset = Coursefile.objects.all()
    serializer_class = CoursefileSerializer


def adminForLogin(request):
    if request.method == 'POST' and request.POST:
        adminname = request.POST.get('admin_name')
        adminpassword = request.POST.get('admin_password')
        obj = Administrator.objects.filter(
            admin_name=adminname, admin_password=adminpassword)
        if obj:
            return JsonResponse({'code': 'ok', 'message': '登录成功'})
        else:
            return JsonResponse({'code': 'no', 'message': '登录失败'})


def ifSignupCamp(request):
    user_id = request.GET.get('user_id')
    camp_id = request.GET.get('camp_id')
    if_signup = Campsignup.objects.filter(user_id=user_id, camp_id=camp_id).first()
    if if_signup:
        return JsonResponse({'statuscode': '200'})
    else:
        return JsonResponse({'statuscode': '400'})


def signupCamp(request):
    user_id = request.GET.get('user_id')
    camp_id = request.GET.get('camp_id')
    class_id = request.GET.get('class_id')
    signupdata = Campsignup(user_id=user_id, camp_id=camp_id, campclass_id=class_id)
    signupdata.save()
    return JsonResponse({'statuscode': '200'})


def createActivity(request):
    if request.method == 'POST' and request.POST:
        obj = Activity.objects.create(activity_name=request.POST.get('activity_name'), activity_time=request.POST.get('activity_time'), activity_location=request.POST.get('activity_location'),
                                      activity_abstract=request.POST.get('activity_abstract'), activity_peopleneed=request.POST.get('activity_peopleneed'), activity_tips=request.POST.get('activity_tips'),
                                      activity_status=request.POST.get('activity_status'), activity_items=request.POST.get('activity_items'))
        obj.save()
        return JsonResponse({'code': '1', 'message': '成功创建活动'})


def modifyActivity(request):
    if request.method == 'POST' and request.POST:
        name = request.POST.get('activity_name')
        time = request.POST.get('activity_time')
        location = request.POST.get('activity_location')
        abstract = request.POST.get('activity_abstract')
        peopleneed = request.POST.get('activity_peopleneed')
        tips = request.POST.get('activity_tips')
        status = request.POST.get('activity_status')
        items = request.POST.get('activity_items')
        obj = Activity.objects.filter(id=request.POST.get('id')).first()
        obj.activity_name = name
        obj.activity_time = time
        obj.activity_location = location
        obj.activity_abstract = abstract
        obj.activity_peopleneed = peopleneed
        obj.activity_tips = tips
        obj.activity_status = status
        obj.activity_items = items
        obj.save()
        return JsonResponse({'code': '1', 'message': '修改成功'})


def addAdministrator(request):
    if request.method == 'POST' and request.POST:
        obj2 = Administrator.objects.filter(
            admin_name=request.POST.get('admin_name'))
        if obj2:
            return JsonResponse({'code': '3', 'message': '用户名已存在'})
        else:
            obj = Administrator.objects.create(admin_name=request.POST.get('admin_name'), admin_password=request.POST.get('admin_password'), power_create_camp=request.POST.get('power_create_camp'), power_create_course=request.POST.get(
                'power_create_course'), power_create_activity=request.POST.get('power_create_activity'), power_create_administrator=request.POST.get('power_create_administrator'))
            obj.save()
            return JsonResponse({'code': '1', 'message': '成功创建管理员'})


def courseinCamp(request):
    camp_id = request.GET.get('camp_id')
    courses = Course.objects.filter(belongto_camp=camp_id)
    course_list = []
    for course in courses:
        serializer = CourseSerializer(course)
        course_list.append(serializer.data)
    return HttpResponse(json.dumps(course_list), content_type="application/json")


def schoolmateData(request):
    schoolmate_id = request.GET.get('schoolmate_id')
    user = User.objects.filter(id=schoolmate_id).first()
    userserializer = UserSerializer(user)
    user_data = []
    user_data.append(userserializer.data)
    return HttpResponse(json.dumps(user_data), content_type="application/json")


def schoolmateMoreData(request):
    schoolmate_id = request.GET.get('schoolmate_id')
    data = Userdata.objects.filter(
        user_id=schoolmate_id).order_by('-id').first()
    dataserializer = UserdataSerializer(data)
    user_data = []
    user_data.append(dataserializer.data)
    return HttpResponse(json.dumps(user_data), content_type="application/json")


def schoolmateCompany(request):
    user_company = request.GET.get('user_company')
    company = Usercompany.objects.filter(id=user_company).first()
    companyserializer = UsercompanySerializer(company)
    user_data = []
    user_data.append(companyserializer.data)
    return HttpResponse(json.dumps(user_data), content_type="application/json")


def getPreviousCampMessage(request):
    if request.method == 'POST' and request.POST:
        id = request.POST.get('id')
        obj_camp = Camp.objects.filter(id=id)
        obj_camp_class = Campclass.objects.get(camp_id=obj_camp.id)
        obj_course = Course.objects.filter(
            belongto_camp=obj_camp.id, belongto_campclass=obj_camp_class.id)
        obj_campSerializer = CampSerializer(obj_camp)
        obj_camp_classSerializer = CampclassSerializer(obj_camp_class)
        obj_courseSerializer = CourseSerializer(obj_course)
        camp_course_data = []
        camp_course_data.append(obj_campSerializer.data)
        camp_course_data.append(obj_camp_classSerializer.data)
        camp_course_data.append(obj_courseSerializer.data)
        return HttpResponse(json.dumps(camp_course_data), content_type="application/json")


def ifinActivity(request):
    attender_id = request.GET.get('attender_id')
    activity_id = request.GET.get('activity_id')
    if_in = Activitytakes.objects.filter(
        attender_id=attender_id, activity_id=activity_id).first()
    if if_in:
        return JsonResponse({'statuscode': '200'})
    else:
        return JsonResponse({'statuscode': '400'})


def attendActivity(request):
    attender_id = request.GET.get('attender_id')
    activity_id = request.GET.get('activity_id')
    new_take = Activitytakes(attender_id=attender_id, activity_id=activity_id)
    new_take.save()
    return JsonResponse({'statuscode': '200'})


def createNewCamp(request):
    if request.method == 'POST' and request.POST:
        name = request.POST.get('name')
        time = request.POST.get('time')
        introduce = request.POST.get('introduce')
        people_oriented = request.POST.get('people_oriented')
        signin_tips = request.POST.get('signin_tips')
        signin_deadline = request.POST.get('signin_deadline')
        permission = request.POST.get('permission')
        obj = Camp.objects.create(name=name, time=time, introduce=introduce,
                                  people_oriented=people_oriented, signin_tips=signin_tips, signin_deadline=signin_deadline, permission=permission)
        obj.save()
        return JsonResponse({'code': '1', 'message': '创建成功'})


def selectSchoolmate(request):
    type = request.GET.get('type')
    content = request.GET.get('content')
    if type == "姓名":
        schoolmates = []
        users = User.objects.filter(user_name=content)
        for user in users:
            schoolmates_serializer = UserSerializer(user)
            schoolmates.append(schoolmates_serializer.data)
    elif type == "地区":
        schoolmates = []
        schoolmates_id = Userdata.objects.filter(
            user_city=content).values_list('user_id').distinct()
        for id in schoolmates_id:
            user = User.objects.filter(user_id=id).first()
            schoolmates_serializer = UserSerializer(user)
            schoolmates.append(schoolmates_serializer.data)
    elif type == "职位":
        schoolmates = []
        schoolmates_id = Userdata.objects.filter(
            user_post=content).values_list('user_id').distinct()
        for id in schoolmates_id:
            user = User.objects.filter(user_id=id).first()
            schoolmates_serializer = UserSerializer(user)
            schoolmates.append(schoolmates_serializer.data)
    else:
        schoolmates = []
        users = User.objects.all()
        for user in users:
            schoolmates_serializer = UserSerializer(user)
            schoolmates.append(schoolmates_serializer.data)
    return HttpResponse(json.dumps(schoolmates), content_type="application/json")


def numberinActivity(request):
    activity_id = request.GET.get('activity_id')
    number = Activitytakes.objects.filter(activity_id=activity_id).count()
    return JsonResponse({'number':number})


def queryAdministrator(request):
    admin = []
    administrators = Administrator.objects.all()
    for administrator in administrators:
        administrator_serializer = AdministratorSerializer(administrator)
        admin.append(administrator_serializer.data)
    return HttpResponse(json.dumps(admin), content_type="application/json")


def specificAdministrator(request):
    specificadmin = []
    name = request.POST.get('name')
    admin = Administrator.objects.filter(admin_name=name).first()
    admin_serializer = AdministratorSerializer(admin)
    specificadmin.append(admin_serializer.data)
    return HttpResponse(json.dumps(specificadmin, ensure_ascii=False), content_type="application/json")


def modifyAdministrator(request):
    table = request.POST.get('admin')
    table_jsoned = json.loads(table)
    Administrator.objects.all().delete()
    i = 0
    while i < len(table_jsoned):
        administrator = Administrator.objects.create(admin_name=table_jsoned[i].get('admin_name'), admin_password=table_jsoned[i].get('admin_password'), power_create_camp=table_jsoned[i].get(
            'power_create_camp'), power_create_course=table_jsoned[i].get('power_create_course'), power_create_activity=table_jsoned[i].get('power_create_activity'), power_create_administrator=table_jsoned[i].get('power_create_administrator'))
        administrator.save()
        i = i+1
    return JsonResponse({'code': '1', 'message': '修改成功'})


def alterUserData(request):
    user_id = request.GET.get('user_id')
    user = User.objects.get(id=user_id)
    user.user_name = request.GET.get('user_name')
    user.user_gender = request.GET.get('user_gender')
    user.user_weixinnumber = request.GET.get('user_weixinnumber')
    user.user_email = request.GET.get('user_email')
    user.save()
    return JsonResponse({'statuscode': '200'})


def alterApplyData(request):
    user_id = request.GET.get('user_id')
    newdata = Userdata.objects.create(user_id=user_id,
                                      user_birthday=request.GET.get(
                                          'user_birthday'),
                                      user_company=request.GET.get(
                                          'user_company'),
                                      user_post=request.GET.get('user_post'),
                                      user_city=request.GET.get('user_city'),
                                      user_referee1_message=request.GET.get(
                                          'user_referee1_message'),
                                      user_referee2_message=request.GET.get(
                                          'user_referee2_message'),
                                      user_referee3_message=request.GET.get(
                                          'user_referee3_message'),
                                      user_other_tips_message_question_for_absenceitem=request.GET.get(
                                          'user_other_tips_message_question_for_absenceitem'),
                                      reasons_for_signin=request.GET.get(
                                          'reasons_for_signin'),
                                      contribution_to_others=request.GET.get(
                                          'contribution_to_others'),
                                      messageway_to_camp=request.GET.get(
                                          'messageway_to_camp'),
                                      educated_condition=request.GET.get(
                                          'educated_condition'),
                                      user_educondition_time_detials=request.GET.get(
                                          'user_educondition_time_detials'),
                                      user_beforestartup_company_condition=request.GET.get(
                                          'user_beforestartup_company_condition'))
    newdata.save()
    update_user = User.objects.filter(id=user_id).first()
    update_user.user_name = request.GET.get('user_name')
    update_user.user_gender = request.GET.get('user_gender')
    update_user.user_weixinnumber = request.GET.get('user_weixinnumber')
    update_user.user_telephone = request.GET.get('user_telephone')
    update_user.user_email = request.GET.get('user_email')
    update_user.save()
    user_company = request.GET.get('user_company')
    update_company = Usercompany.objects.filter(
        brand_name=user_company).first()
    if not update_company:
        update_company = Usercompany(brand_name=user_company)
    update_company.website = request.GET.get('website')
    update_company.app_or_publicAccounts = request.GET.get(
        'app_or_publicAccounts')
    update_company.startup_time = request.GET.get('startup_time')
    update_company.center_city = request.GET.get('center_city')
    update_company.membership = request.GET.get('membership')
    update_company.abstract = request.GET.get('abstract')
    update_company.main_operational_data = request.GET.get(
        'main_operational_data')
    update_company.income_scale = request.GET.get('income_scale')
    update_company.financing_situation = request.GET.get('financing_situation')
    update_company.value_of_assessment = request.GET.get('value_of_assessment')
    update_company.additions = request.GET.get('additions')
    update_company.save()
    return JsonResponse({'statuscode': '200'})


def weixinLogin(request):
    user_telephone = request.GET.get('user_telephone')
    if_registered = User.objects.filter(user_telephone=user_telephone).first()
    if if_registered:
        clnt = YunpianClient('70b37503044891ec90e2b5da3f0a5fb1')
        auth_code = str(random.randint(100000, 999999))
        param = {YC.MOBILE: user_telephone, YC.TEXT: '【云片网】您的验证码是'+auth_code}
        r = clnt.sms().single_send(param)
        if r:
            return JsonResponse({'auth_code': auth_code, 'statuscode': '200'})
        else:
            return JsonResponse({'auth_code': auth_code, 'statuscode': '400'})
    else:
        return JsonResponse({'auth_code': '000000', 'statuscode': '400'})


def weixinRegister(request):
    user_telephone = request.GET.get('user_telephone')
    if_registered = User.objects.filter(user_telephone=user_telephone).first()
    if not if_registered:
        clnt = YunpianClient('70b37503044891ec90e2b5da3f0a5fb1')
        auth_code = str(random.randint(100000, 999999))
        param = {YC.MOBILE: user_telephone, YC.TEXT: '【云片网】您的验证码是'+auth_code}
        r = clnt.sms().single_send(param)
        if r:
            return JsonResponse({'auth_code': auth_code, 'statuscode': '200'})
        else:
            return JsonResponse({'auth_code': auth_code, 'statuscode': '400'})
    else:
        return JsonResponse({'auth_code': '000000', 'statuscode': '400'})


def weixinAddUser(request):
    user_telephone = request.GET.get('user_telephone')
    newuser = User(user_telephone=user_telephone)
    newuser.save()
    return JsonResponse({'statuscode': '200'})


def initializeData(request):
    user_telephone = request.GET.get('user_telephone')
    new_user = User.objects.filter(user_telephone=user_telephone).first()
    if not new_user:
        return JsonResponse({'statuscode': '400'})
    new_user.user_name = request.GET.get('user_name')
    new_user.user_weixinnumber = request.GET.get('user_weixinnumber')
    new_user.user_gender = request.GET.get('user_gender')
    new_user.user_email = request.GET.get('user_email')
    new_user.save()
    return JsonResponse({'statuscode': '200'})


def changeTelephone(request):
    user_telephone = request.GET.get('user_telephone')
    if_registered = User.objects.filter(user_telephone=user_telephone).first()
    if not if_registered:
        clnt = YunpianClient('70b37503044891ec90e2b5da3f0a5fb1')
        auth_code = str(random.randint(100000, 999999))
        param = {YC.MOBILE: user_telephone, YC.TEXT: '【云片网】您的验证码是'+auth_code}
        r = clnt.sms().single_send(param)
        if r:
            return JsonResponse({'auth_code': auth_code, 'statuscode': '200'})
        else:
            return JsonResponse({'auth_code': auth_code, 'statuscode': '400'})
    else:
        return JsonResponse({'auth_code': '000000', 'statuscode': '400'})


def querySchoolmate(request):
    camptakes = []
    campattends = Campattend.objects.all()
    for campattend in campattends:
        campattend_serializer = CampattendSerializer(campattend)
        camptakes.append(campattend_serializer.data)
        user = User.objects.filter(id=campattend_serializer.data.get('user_id')).first()
        user_serializer = UserSerializer(user)
        camptakes.append(user_serializer.data)
        campsignup = Campsignup.objects.filter(user_id=campattend_serializer.data.get('user_id'),camp_id=campattend_serializer.data.get('camp_id')).first()
        campsignup_serializer = CampsignupSerializer(campsignup)
        camptakes.append(campsignup_serializer.data)
        campclass = Campclass.objects.filter(id=campsignup_serializer.data.get('campclass_id')).first()
        campclass_serializer = CampclassSerializer(campclass)
        camptakes.append(campclass_serializer.data)
        camp = Camp.objects.filter(id=campattend_serializer.data.get('camp_id')).first()
        camp_serializer = CampSerializer(camp)
        camptakes.append(camp_serializer.data)
    return HttpResponse(json.dumps(camptakes), content_type="application/json")


def selectSpecificSchoolmate(request):
    if request.method == 'POST' and request.POST:
        specificmsg = []
        Id = request.POST.get('id')
        user = User.objects.filter(id=Id).first()
        userdata = Userdata.objects.filter(user_id=user.id).first()
        usercompany = Usercompany.objects.filter(
            id=userdata.user_company).first()
        user_serializer = UserSerializer(user)
        specificmsg.append(user_serializer.data)
        userdata_serializer = UserdataSerializer(userdata)
        specificmsg.append(userdata_serializer.data)
        usercompany_serializer = UsercompanySerializer(usercompany)
        specificmsg.append(usercompany_serializer.data)
        return HttpResponse(json.dumps(specificmsg, ensure_ascii=False), content_type="application/json")


def queryCampSignup(request):
    camp_id = int(request.POST.get('camp_id'))
    objs = Campsignup.objects.filter(camp_id=camp_id).order_by('id')
    signuplist = []
    for obj in objs:
        user = User.objects.get(id=obj.user_id)
        user_serializer = UserSerializer(user)
        signuplist.append(user_serializer.data)
        userdata = Userdata.objects.filter(user_id=user.id).last()
        usercompany = Usercompany.objects.get(id=userdata.user_company)
        if_userattend = len(Campattend.objects.filter(
            camp_id=camp_id, user_id=user.id))
        signuplist.append(usercompany.name)
        signuplist.append(userdata.user_post)
        campclass = Campclass.objects.get(id=obj.campclass_id)
        signuplist.append(campclass.name)
        signuplist.append(if_userattend)
    return HttpResponse(json.dumps(signuplist, ensure_ascii=False), content_type="application/json")


def modifyCampattend(request):
    modifydata = request.POST.get('users')
    modifydata_jsoned = json.loads(modifydata)
    temp = 0
    while temp < len(modifydata_jsoned):
        if modifydata_jsoned[temp].get('status') == 1:
            userattend = Campattend.objects.create(user_id=modifydata_jsoned[temp].get(
                'user_id'), camp_id=modifydata_jsoned[temp].get('camp_id'))
            userattend.save()
        elif modifydata_jsoned[temp].get('status') == 0:
            Campattend.objects.filter(user_id=modifydata_jsoned[temp].get(
                'user_id'), camp_id=modifydata_jsoned[temp].get('camp_id')).delete()
        temp = temp+1
    return JsonResponse({'code': '1', 'message': '修改成功'})


def queryCamps(request):
    camplist = []
    camps = Camp.objects.all()
    for camp in camps:
        camp_serializer = CampSerializer(camp)
        camplist.append(camp_serializer.data)
    return HttpResponse(json.dumps(camplist, ensure_ascii=False), content_type="application/json")


def specificCampMsg(request):
    specificcampmsg = []
    Id = int(request.POST.get('id'))
    camp = Camp.objects.filter(id=Id).first()
    signup_number = len(Campsignup.objects.filter(camp_id=Id))
    attend_number = len(Campattend.objects.filter(camp_id=Id))
    camp_serializer = CampSerializer(camp)
    specificcampmsg.append(camp_serializer.data)
    specificcampmsg.append(signup_number)
    specificcampmsg.append(attend_number)
    return HttpResponse(json.dumps(specificcampmsg, ensure_ascii=False), content_type="application/json")


def modifyCampMsg(request):
    Id = int(request.POST.get('id'))
    obj = Camp.objects.filter(id=Id).first()
    obj.name = request.POST.get('name')
    obj.time = request.POST.get('time')
    obj.introduce = request.POST.get('introduce')
    obj.people_oriented = request.POST.get('people_oriented')
    obj.signin_tips = request.POST.get('signin_tips')
    obj.signin_deadline = request.POST.get('signin_deadline')
    obj.permission = request.POST.get('permission')
    obj.save()
    return JsonResponse({'code': '1', 'message': '修改成功'})


def queryActivity(request):
    activitylist = []
    activities = Activity.objects.all()
    for activity in activities:
        activity_serializer = ActivitySerializer(activity)
        activitylist.append(activity_serializer.data)
    return HttpResponse(json.dumps(activitylist, ensure_ascii=False), content_type="application/json")


def specificActivityMsg(request):
    specificactivitymsg = []
    Id = int(request.POST.get('id'))
    activity = Activity.objects.filter(id=Id).first()
    attend_number = len(Activitytakes.objects.filter(activity_id=Id))
    activity_serializer = ActivitySerializer(activity)
    specificactivitymsg.append(activity_serializer.data)
    specificactivitymsg.append(attend_number)
    return HttpResponse(json.dumps(specificactivitymsg, ensure_ascii=False), content_type="application/json")


def queryActivityAttenders(request):
    Id = int(request.POST.get('id'))
    attenders = Activitytakes.objects.filter(activity_id=Id).order_by('id')
    attenderlist = []
    for attender in attenders:
        user = User.objects.get(id=attender.attender_id)
        user_serializer = UserSerializer(user)
        attenderlist.append(user_serializer.data)
    return HttpResponse(json.dumps(attenderlist, ensure_ascii=False), content_type="application/json")


def getId(request):
    user_telephone = request.GET.get('user_telephone')
    user = User.objects.filter(user_telephone=user_telephone).first()
    user_serializer = UserSerializer(user)
    user_id = user_serializer.data['id']
    return JsonResponse({'user_id': user_id})


def createCampClass(request):
    if request.method == 'POST' and request.POST:
        obj = Campclass.objects.create(name=request.POST.get('class_name'), student_number=request.POST.get(
            'class_number'), camp_id=request.POST.get('camp_id'))
        obj.save()
        return JsonResponse({'code': '1', 'message': '成功创建班级'})


def queryCampClass(request):
    if request.method == 'POST' and request.POST:
        campId = int(request.POST.get('camp_id'))
        Class = []
        campClasses = Campclass.objects.filter(camp_id=campId)
        for campClass in campClasses:
            campClass_serializer = CampclassSerializer(campClass)
            Class.append(campClass_serializer.data)
        return HttpResponse(json.dumps(Class), content_type="application/json")


def deleteCampclass(request):
    if request.method == 'POST' and request.POST:
        deleteId = int(request.POST.get('class_id'))
        obj = Campclass.objects.filter(id=deleteId)
        obj.delete()
    return JsonResponse({'code': '1', 'message': '删除班级成功'})


def queryCourseCamp(request):
    camplist = []
    camps = Camp.objects.all()
    for camp in camps:
        camp_serializer = CampSerializer(camp)
        camplist.append(camp_serializer.data)
    return HttpResponse(json.dumps(camplist, ensure_ascii=False), content_type="application/json")


def specificClassMsg(request):
    if request.method == 'POST' and request.POST:
        campId = int(request.POST.get('camp_id'))
        Class = []
        campClasses = Campclass.objects.filter(camp_id=campId)
        for campClass in campClasses:
            campClass_serializer = CampclassSerializer(campClass)
            Class.append(campClass_serializer.data)
        return HttpResponse(json.dumps(Class), content_type="application/json")


def addLesson(request):
    obj = Course.objects.create(name=request.POST.get('name'), time=request.POST.get('time'), location=request.POST.get('location'), teacher=request.POST.get('teacher'), abstract=request.POST.get(
        'abstract'), belongto_camp=request.POST.get('belongto_camp'), belongto_campclass=request.POST.get('belongto_campclass'), number_bystander=request.POST.get('number_bystander'), bystand_tips=request.POST.get('bystand_tips'))
    obj.save()
    return JsonResponse({'code': '1', 'message': '成功创建'})


def specificLessonList(request):
    if request.method == 'POST' and request.POST:
        belongtocampclass = request.POST.get('belongto_campclass')
        returnTable = []
        lessons = Course.objects.filter(belongto_campclass=belongtocampclass)
        for lesson in lessons:
            lesson_ser = CourseSerializer(lesson)
            returnTable.append(lesson_ser.data)
        return HttpResponse(json.dumps(returnTable), content_type="application/json")


def operateFiles(request):
    print(request.POST)
    print(request.FILES)
    Id = request.POST.get('id')
    ppt_name = request.POST.get('ppt_name', '')
    ppt = request.FILES.get('ppt', '')
    video_name = request.POST.get('video_name', '')
    video = request.FILES.get('video', '')
    text_name = request.POST.get('text_name', '')
    text = request.FILES.get('text', '')
    others_name = request.POST.get('others_name', '')
    others = request.FILES.get('others', '')
    obj = Coursefile.objects.filter(course_id=Id).first()
    if obj:
        if ppt_name:
            obj.ppt_name = ppt_name
        if ppt:
            obj.ppt = ppt
        if video_name:
            obj.video_name = video_name
        if video:
            obj.video = video
        if text_name:
            obj.text_name = text_name
        if text:
            obj.text = text
        if others_name:
            obj.others_name = others_name
        if others:
            obj.others = others
        obj.save()
        return JsonResponse({'code': '1'})
    else:
        newobj = Coursefile.objects.create(course_id=Id, ppt_name=ppt_name, ppt=ppt, video_name=video_name,
                                           video=video, text_name=text_name, text=text, others_name=others_name, others=others)
        newobj.save()
    return JsonResponse({'code': '1'})


def getCoursefileName(request):
    id = int(request.POST.get('id'))
    obj = Coursefile.objects.filter(course_id=id).first()
    data = []
    data.append({'ppt_name': obj.ppt_name})
    data.append({'video_name': obj.video_name})
    data.append({'text_name': obj.text_name})
    data.append({'others_name': obj.others_name})
    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json')


def modifyCourse(request):
    if request.method == 'POST' and request.POST:
        course_name = request.POST.get('name')
        course_time = request.POST.get('time')
        course_location = request.POST.get('location')
        course_teacher = request.POST.get('teacher')
        course_abstract = request.POST.get('abstract')
        belongto_camp = request.POST.get('belongto_camp')
        belongto_campclass = request.POST.get('belongto_campclass')
        number_bystander = request.POST.get('number_bystander')
        bystand_tips = request.POST.get('bystand_tips')
        obj = Course.objects.filter(id=request.POST.get('id')).first()
        obj.name = course_name
        obj.time = course_time
        obj.location = course_location
        obj.teacher = course_teacher
        obj.abstract = course_abstract
        obj.belongto_camp = belongto_camp
        obj.belongto_campclass = belongto_campclass
        obj.number_bystander = number_bystander
        obj.bystand_tips = bystand_tips
        obj.save()
        return JsonResponse({'code': '1', 'message': '修改成功'})


def getFiles(request):
    courses = request.GET.get('courses')
    print(request.GET)
    files = []
    courses = json.loads(courses)
    for course in courses:
        course_file = Coursefile.objects.get(course_id=int(course['id']))
        file_serializer = CoursefileSerializer(course_file)
        files.append(file_serializer.data)
    return HttpResponse(json.dumps(files, ensure_ascii=False),content_type='application/json')
        