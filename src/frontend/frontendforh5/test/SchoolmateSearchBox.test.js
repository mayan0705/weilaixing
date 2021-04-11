import { mount } from '@vue/test-utils'
import SchoolmateSearchBox from '@/components/SchoolmateSearchBox'
import Vue from 'vue'
import ElementUI from 'element-ui'
Vue.use(ElementUI)

test('renders correctly', () => {
  const wrapper = mount(SchoolmateSearchBox)
  expect(wrapper.element).toMatchSnapshot()
})