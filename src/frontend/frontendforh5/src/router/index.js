import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/pages/Index'
import RegistrationManagePage from '@/pages/RegistrationManagePage'
import ClassManagePage from '@/pages/ClassManagePage'
import ActivityManagePage from '@/pages/ActivityManagePage'
import SchoolmatePage from '@/pages/SchoolmatePage'
import SuperuserManagePage from '@/pages/SuperuserManagePage'
import CreateNewCamp from '@/components/CreateNewCamp'
import PioneerCampForm from '@/components/PioneerCampForm'
import PioneerCampUserInformation from '@/components/PioneerCampUserInformation'
import CourseInfoForm from '@/components/CourseInfoForm'
import ActivityInfoForm from '@/components/ActivityInfoForm'
import ActivityFillingForm from '@/components/ActivityFillingForm'
import SmInfoForm from '@/components/SmInfoForm'
import AddicantInformation from '@/components/AddicantInformation'
import CourseInformation from '@/components/CourseInformation'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/RegistrationManagePage',
      name: 'RegistrationManagePage',
      component: RegistrationManagePage
    },
    {
      path: '/ClassManagePage',
      name: 'ClassManagePage',
      component: ClassManagePage
    },
    {
      path: '/ActivityManagePage',
      name: 'ActivityManagePage',
      component: ActivityManagePage
    },
    {
      path: '/SchoolmatePage',
      name: 'SchoolmatePage',
      component: SchoolmatePage
    },
    {
      path: '/SuperuserManagePage',
      name: 'SuperuserManagePage',
      component: SuperuserManagePage
    },
    {
      path: '/RegistrationManagePage/CreateNewCamp',
      name: 'CreateNewCamp',
      component: CreateNewCamp
    },
    {
      path: '/RegistrationManagePage/PioneerCampForm',
      name: 'PioneerCampForm',
      component: PioneerCampForm
    },
    {
      path: '/RegistrationManagePage/PioneerCampForm/PioneerCampUserInformation',
      name: 'PioneerCampUserInformation',
      component: PioneerCampUserInformation
    },
    {
      path: '/ClassManagePage/CourseInfoForm',
      name: 'CourseInfoForm',
      component: CourseInfoForm
    },
    {
      path: '/ActivityManagePage/ActivityInfoForm',
      name: 'ActivityInfoForm',
      component: ActivityInfoForm
    },
    {
      path: '/ActivityManagePage/ActivityFillingForm',
      name: 'ActivityFillingForm',
      component: ActivityFillingForm
    },
    {
      path: '/SchoolmatePage/SmInfoForm',
      name: 'SmInfoForm',
      component: SmInfoForm
    },
    {
      path: '/RegistrationManagePage/PioneerCampForm/PioneerCampUserInformation/AddicantInformation',
      name: 'AddicantInformation',
      component: AddicantInformation,
    },
    {
      path: '/ClassManagePage/CourseInfoForm/CourseInformation',
      name: 'CourseInformation',
      component: CourseInformation,
    }
  ]
})