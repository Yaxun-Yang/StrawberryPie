import Vue from 'vue'
import {
    Button, Form, FormItem, Input, Message, Container, Row, Col, Dialog,
    Header, Aside, Main, Menu, Submenu, MenuItemGroup, MenuItem, Breadcrumb, BreadcrumbItem,
    Avatar ,Card, Upload, Progress, DatePicker, MessageBox, Image,
    Table, TableColumn, Pagination,TimePicker,  TimeSelect,Switch,
    Divider,
    Slider,
    Popover,
    Select,
    Option,
    Alert

} from 'element-ui'

//变为全局可用
Vue.use(Button)
Vue.use(Form)
Vue.use(FormItem)
Vue.use(Input)
Vue.use(Container)
Vue.use(Header)
Vue.use(Main)
Vue.use(Aside)
Vue.use(Menu)
Vue.use(Submenu)
Vue.use(MenuItem)
Vue.use(MenuItemGroup)
Vue.use(Breadcrumb)
Vue.use(BreadcrumbItem)
Vue.use(Avatar)
Vue.use(Card)
Vue.use(Row)
Vue.use(Col)
Vue.use(Dialog)
Vue.use(Upload)
Vue.use(Progress)
Vue.use(TimePicker)
Vue.use(DatePicker)
Vue.use(Image)
Vue.use(Table)
Vue.use(TableColumn)
Vue.use(Pagination)
Vue.use(TimeSelect)
Vue.use(Switch)
Vue.use(Divider)
Vue.use(Slider)
Vue.use(Popover)
Vue.use(Select)
Vue.use(Option)
Vue.use(Alert)

//导入弹框提示组建
Vue.prototype.$message = Message
Vue.prototype.$confirm = MessageBox.confirm
