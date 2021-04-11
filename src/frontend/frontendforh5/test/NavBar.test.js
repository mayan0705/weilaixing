import { mount } from '@vue/test-utils'
import NavBar from '@/components/NavBar'
import Vue from 'vue'
import ElementUI from 'element-ui'
Vue.use(ElementUI)

test('renders correctly', () => {
  const wrapper = mount(NavBar)
  expect(wrapper.element).toMatchSnapshot()
})