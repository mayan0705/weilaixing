import { mount } from '@vue/test-utils'
import RegistrationManagePage from '@/pages/RegistrationManagePage'
import Vue from 'vue'
import ElementUI from 'element-ui'
Vue.use(ElementUI)

test('renders correctly', () => {
  const wrapper = mount(RegistrationManagePage)
  expect(wrapper.element).toMatchSnapshot()
})