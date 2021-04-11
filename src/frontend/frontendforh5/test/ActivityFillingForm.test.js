import { mount } from '@vue/test-utils'
import ActivityFillingForm from '@/components/ActivityFillingForm'
import Vue from 'vue'
import ElementUI from 'element-ui'
Vue.use(ElementUI)

test('renders correctly', () => {
  const wrapper = mount(ActivityFillingForm)
  expect(wrapper.element).toMatchSnapshot()
})