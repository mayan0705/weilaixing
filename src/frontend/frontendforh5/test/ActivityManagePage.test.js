import { mount } from '@vue/test-utils'
import ActivityManagePage from '@/pages/ActivityManagePage'
import Vue from 'vue'
import ElementUI from 'element-ui'
Vue.use(ElementUI)

test('renders correctly', () => {
  const wrapper = mount(ActivityManagePage)
  expect(wrapper.element).toMatchSnapshot()
})