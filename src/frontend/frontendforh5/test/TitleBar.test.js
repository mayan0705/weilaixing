import { mount } from '@vue/test-utils'
import TitleBar from '@/components/TitleBar'
import Vue from 'vue'
import ElementUI from 'element-ui'
Vue.use(ElementUI)

test('renders correctly', () => {
  const wrapper = mount(TitleBar)
  expect(wrapper.element).toMatchSnapshot()
})