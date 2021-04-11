import { mount } from '@vue/test-utils'
import PioneerCampForm from '@/components/PioneerCampForm'
import Vue from 'vue'
import ElementUI from 'element-ui'
Vue.use(ElementUI)

test('renders correctly', () => {
  const wrapper = mount(PioneerCampForm)
  expect(wrapper.element).toMatchSnapshot()
})