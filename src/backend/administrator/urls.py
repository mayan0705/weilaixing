from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls import *

router = routers.DefaultRouter()
router.register('Administrator', views.AdministratorView)
router.register('Campclass', views.CampclassView)
router.register('Camp', views.CampView)
router.register('Course', views.CourseView)
router.register('Coursebystander', views.CoursebystanderView)
router.register('Campsignup', views.CampsignupView)
router.register('Campattendup', views.CampattendView)
router.register('User', views.UserView)
router.register('Userdata', views.UserdataView)
router.register('Usercompany', views.UsercompanyView)
router.register('Activity', views.ActivityView)
router.register('Activitytakes', views.ActivitytakesView)
router.register('Coursefile', views.CoursefileView)
urlpatterns = [
    path('', include(router.urls)),
    url(r'adminForLogin/', views.adminForLogin, name='adminForLogin'),
    url(r'ifSignupCamp/', views.ifSignupCamp),
    url(r'signupCamp/', views.signupCamp),
    url(r'createActivity/', views.createActivity, name='createActivity'),
    url(r'addAdministrator/', views.addAdministrator, name='addAdministrator'),
    url(r'courseinCamp/', views.courseinCamp, name='courseinCamp'),
    url(r'schoolmateData/', views.schoolmateData, name='schoolmateData'),
    url(r'modifyActivity/', views.modifyActivity, name='modifyActivity'),
    url(r'getPreviousCampMessage/', views.getPreviousCampMessage,
        name='getPreviousCampMessage'),
    url(r'ifinActivity/', views.ifinActivity, name='ifinActivity'),
    url(r'attendActivity/', views.attendActivity, name='attendActivity'),
    url(r'createNewCamp/', views.createNewCamp, name='createNewCamp'),
    url(r'selectSchoolmate/', views.selectSchoolmate, name='selectSchoolmate'),
	url(r'schoolmateMoreData/', views.schoolmateMoreData, name='schoolmateMoreData'),
	url(r'schoolmateCompany/', views.schoolmateCompany, name='schoolmateCompany'),
    url(r'queryAdministrator/', views.queryAdministrator, name='queryAdministrator'),
    url(r'modifyAdministrator/', views.modifyAdministrator,
        name='modifyAdministrator'),
    url(r'alterApplyData/', views.alterApplyData, name='alterApplyData'),
    url(r'alterUserData/', views.alterUserData, name='alterUserData'),
    url(r'weixinLogin/', views.weixinLogin, name='weixinLogin'),
    url(r'weixinRegister/', views.weixinRegister, name='weixinRegister'),
    url(r'initializeData/', views.initializeData, name='initializeData'),
    url(r'changeTelephone/', views.changeTelephone, name='changeTelephone'),
    url(r'querySchoolmate/', views.querySchoolmate, name='querySchoolmate'),
    url(r'selectSpecificSchoolmate/', views.selectSpecificSchoolmate,
        name='selectSpecificSchoolmate'),
    url(r'queryCampSignup/', views.queryCampSignup, name='queryCampSignup'),
    url(r'queryCamps/', views.queryCamps, name='queryCamps'),
    url(r'specificCampMsg/', views.specificCampMsg, name='specificCampMsg'),
    url(r'modifyCampMsg/', views.modifyCampMsg, name='modifyCampMsg'),
    url(r'queryActivity/', views.queryActivity, name='queryActivity'),
    url(r'specificActivityMsg/', views.specificActivityMsg,
        name='specificActivityMsg'),
    url(r'weixinAddUser/', views.weixinAddUser, name='weixinAddUser'),
    url(r'getId/', views.getId, name='getId'),
    url(r'createCampClass/', views.createCampClass, name='createCampClass'),
    url(r'queryCampClass/', views.queryCampClass, name='queryCampClass'),
    url(r'modifyCampattend/', views.modifyCampattend, name='modifyCampattend'),
    url(r'deleteCampclass/', views.deleteCampclass, name='deleteCampclass'),
    url(r'queryCourseCamp/', views.queryCourseCamp, name='queryCourseCamp'),
    url(r'specificClassMsg/', views.specificClassMsg, name='specificClassMsg'),
    url(r'addLesson/', views.addLesson, name='addLesson'),
    url(r'specificLessonList/', views.specificLessonList, name='specificLessonList'),
    url(r'specificAdministrator/', views.specificAdministrator,
        name='specificAdministrator'),
    url(r'queryActivityAttenders/', views.queryActivityAttenders,
        name='queryActivityAttenders'),
    url(r'operateFiles/', views.operateFiles, name='operateFiles'),
    url(r'getCoursefileName/', views.getCoursefileName, name='getCoursefileName'),
    url(r'modifyCourse/', views.modifyCourse, name='modifyCourse'),
    url(r'getFiles/', views.getFiles, name='getFiles'),
]
