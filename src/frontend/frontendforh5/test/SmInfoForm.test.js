import { mount } from '@vue/test-utils'
import SmInfoForm from '@/components/SmInfoForm'
import Vue from 'vue'
import ElementUI from 'element-ui'
Vue.use(ElementUI)

test('renders correctly', () => {
  const wrapper = mount(SmInfoForm)
  expect(wrapper.element).toMatchSnapshot()
})