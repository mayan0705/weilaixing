import { mount } from '@vue/test-utils'
import SchoolmateTable from '@/components/SchoolmateTable'
import Vue from 'vue'
import ElementUI from 'element-ui'
Vue.use(ElementUI)

test('renders correctly', () => {
  const wrapper = mount(SchoolmateTable)
  expect(wrapper.element).toMatchSnapshot()
})