import { mount } from '@vue/test-utils'
import ActivityInfoForm from '@/components/ActivityInfoForm'
import Vue from 'vue'
import ElementUI from 'element-ui'
Vue.use(ElementUI)

test('renders correctly', () => {
  const wrapper = mount(ActivityInfoForm)
  expect(wrapper.element).toMatchSnapshot()
})