import { mount } from '@vue/test-utils'
import SchoolmatePage from '@/pages/SchoolmatePage'
import Vue from 'vue'
import ElementUI from 'element-ui'
Vue.use(ElementUI)

test('renders correctly', () => {
  const wrapper = mount(SchoolmatePage)
  expect(wrapper.element).toMatchSnapshot()
})