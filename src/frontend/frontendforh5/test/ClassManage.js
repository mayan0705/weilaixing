import { mount } from '@vue/test-utils'
import ClassManage from '@/components/ClassManage'
import Vue from 'vue'
import ElementUI from 'element-ui'
Vue.use(ElementUI)

test('renders correctly', () => {
  const wrapper = mount(ClassManage)
  expect(wrapper.element).toMatchSnapshot()
})