import { mount } from '@vue/test-utils'
import AddicantInformation from '@/components/AddicantInformation'
import Vue from 'vue'
import ElementUI from 'element-ui'
Vue.use(ElementUI)

test('renders correctly', () => {
  const wrapper = mount(AddicantInformation)
  expect(wrapper.element).toMatchSnapshot()
})