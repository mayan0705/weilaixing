import { mount } from '@vue/test-utils'
import CreateNewCamp from '@/components/CreateNewCamp'
import Vue from 'vue'
import ElementUI from 'element-ui'
Vue.use(ElementUI)

test('renders correctly', () => {
  const wrapper = mount(CreateNewCamp)
  expect(wrapper.element).toMatchSnapshot()
})