import { mount } from '@vue/test-utils'
import CourseInfoForm from '@/components/CourseInfoForm'
import Vue from 'vue'
import ElementUI from 'element-ui'
Vue.use(ElementUI)

test('renders correctly', () => {
  const wrapper = mount(CourseInfoForm)
  expect(wrapper.element).toMatchSnapshot()
})