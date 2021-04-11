import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        id: '',
        pwd: '',
        name: '',
        campIndex: 0,
        activityIndex: 0,
        campStatus: false,
        activityStatus: false,
        signinStatus: false,
        schoolmateIndex: 0,
        schoolmateCampIndex: 0,
        schoolmateCampClassIndex: 0,
        addicantIndex: 0,
        powerCamp: 'false',
        powerCourse: 'false',
        powerActivity: 'false',
        powerAdministrator: 'false',
        newCampCreatable: 'false',
        courseId: 0,
        classId: 0
    },
    mutations: {
        setId(state, id) {
            state.id = id
            sessionStorage.setItem('id', id)
        },
        setName(state, name) {
            state.name = name
            localStorage.setItem('name', name)
        },
        setPwd(state, pwd) {
            state.pwd = pwd
            localStorage.setItem('pwd', pwd)
        },
        setCampIndex(state, campIndex) {
            state.campIndex = campIndex
            sessionStorage.setItem('campIndex', campIndex)
        },
        setCampStatus(state, campStatus) {
            state.campStatus = campStatus
            sessionStorage.setItem('campStatus', campStatus)
        },
        setActivityIndex(state, activityIndex) {
            state.activityIndex = activityIndex
            sessionStorage.setItem('activityIndex', activityIndex)
        },
        setSigninStatus(state, signinStatus) {
            state.signinStatus = signinStatus
            sessionStorage.setItem('signinStatus', signinStatus)
        },
        setActivityStatus(state, activityStatus) {
            state.activityStatus = activityStatus
            sessionStorage.setItem('activityStatus', activityStatus)
        },
        setSchoolmateIndex(state, schoolmateIndex) {
            state.schoolmateIndex = schoolmateIndex
            sessionStorage.setItem('schoolmateIndex', schoolmateIndex)
        },
        setAddicantIndex(state, addicantIndex) {
            state.addicantIndex = addicantIndex
            sessionStorage.setItem('addicantIndex', addicantIndex)
        },
        setSchoolmateCampIndex(state, schoolmateCampIndex) {
            state.schoolmateCampIndex = schoolmateCampIndex
            sessionStorage.setItem('schoolmateCampIndex', schoolmateCampIndex)
        },
        setSchoolmateCampClassIndex(state, schoolmateCampClassIndex) {
            state.schoolmateCampClassIndex = schoolmateCampClassIndex
            sessionStorage.setItem('schoolmateCampClassIndex', schoolmateCampClassIndex)
        },
        setPowerCamp(state, powerCamp) {
            state.powerCamp = powerCamp
            localStorage.setItem('powerCamp', powerCamp)
        },
        setPowerCourse(state, powerCourse) {
            state.powerCourse = powerCourse
            localStorage.setItem('powerCourse', powerCourse)
        },
        setPowerActivity(state, powerActivity) {
            state.powerActivity = powerActivity
            localStorage.setItem('powerActivity', powerActivity)
        },
        setPowerAdministrator(state, powerAdministrator) {
            state.powerAdministrator = powerAdministrator
            localStorage.setItem('powerAdministrator', powerAdministrator)
        },
        setNewCampCreatable(state, newCampCreatable) {
            state.newCampCreatable = newCampCreatable
            localStorage.setItem('newCampCreatable', newCampCreatable)
        },
        setCourseId(state, courseId) {
            state.courseId = courseId
            sessionStorage.setItem('courseId', courseId)
        },
        setClassId(state, classId) {
            state.classId = classId
            sessionStorage.setItem('classId', classId)
        }
    },
    getters: {
        id: (state) => sessionStorage.getItem('id'),
        name: (state) => localStorage.getItem('name'),
        pwd: (state) => localStorage.getItem('pwd'),
        campIndex: (state) => sessionStorage.getItem('campIndex'),
        campStatus: (state) => sessionStorage.getItem('campStatus'),
        activityIndex: (state) => sessionStorage.getItem('activityIndex'),
        signinStatus: (state) => sessionStorage.getItem('signinStatus'),
        activityStatus: (state) => sessionStorage.getItem('activityStatus'),
        schoolmateIndex: (state) => sessionStorage.getItem('schoolmateIndex'),
        addicantIndex: (state) => sessionStorage.getItem('addicantIndex'),
        powerCamp: (state) => localStorage.getItem('powerCamp'),
        powerCourse: (state) => localStorage.getItem('powerCourse'),
        powerActivity: (state) => localStorage.getItem('powerActivity'),
        powerAdministrator: (state) => localStorage.getItem('powerAdministrator'),
        newCampCreatable: (state) => localStorage.getItem('newCampCreatable'),
        schoolmateCampIndex: (state) => sessionStorage.getItem('schoolmateCampIndex'),
        schoolmateCampClassIndex: (state) => sessionStorage.getItem('schoolmateCampClassIndex'),
        courseId: (state) => sessionStorage.getItem('courseId'),
        classId: (state) => sessionStorage.getItem('classId'),
    }
})