import { mount } from '@vue/test-utils'
import SuperUserManageTable from '@/components/SuperUserManageTable'
import Vue from 'vue'
import ElementUI from 'element-ui'
Vue.use(ElementUI)

test('renders correctly', () => {
  const wrapper = mount(SuperUserManageTable)
  expect(wrapper.element).toMatchSnapshot()
})