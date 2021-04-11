import { mount } from '@vue/test-utils'
import SuperuserManagePage from '@/pages/SuperuserManagePage'
import Vue from 'vue'
import ElementUI from 'element-ui'
Vue.use(ElementUI)

test('renders correctly', () => {
  const wrapper = mount(SuperuserManagePage)
  expect(wrapper.element).toMatchSnapshot()
})