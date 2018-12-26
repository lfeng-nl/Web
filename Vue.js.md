## 1.Vue基础

### 1.实例

```js
var vm = new Vue({
    el: "#n_id",
    data: {
        name: 'xxx'
    },
    // 声明周期钩子, create
    create: function () {
        console.log('xxx');
    }
})
```

- 只有Vue实例被创建时`data`中存在的属性才是响应式的; 这些数据改变时, 试图会进行重渲染;
- `Vue`实例还会暴露一些`$`前缀的属性和方法, 具有特殊作用和功能, 详见 [API](https://cn.vuejs.org/v2/api/#%E5%AE%9E%E4%BE%8B%E5%B1%9E%E6%80%A7)
- 生命周期钩子:
  - `beforeCreate`: 实例创建前,
  - `create`, 在实例创建时调用;
  - `mounted`: 编译好的HTML挂载到页面完成后, 会做些ajax请求获取数据进行数据初始化,
  - `updated`: 数据变化更新DOM后;
  - [参看](https://segmentfault.com/a/1190000008570622):![Vue生命周期](https://segmentfault.com/img/remote/1460000012510450)

### 2.模板语法

- 文本: `{{ msg }}`
- 原始HTML: `<div v-html="rawHtml"></div>` --> `<div> xxxxxx </div>`
- 作用于特性: `<div v-bing:id="dynamicId"></div>`

> 以上都支持JavaScript表达式

### 3.计算属性和侦听器

- 计算属性: 属性值由计算得出, 只要依赖值未发生变化就使用缓存值, 发生变化后才进行二次计算;

  ```js
  computed: {
      msg_c: function() {
          // 当 msg 属性值改变时, msg_c 会重新计算的出新的值
          return this.msg[0];  
      }
  }
  ```

  - 计算属性默认只有`getter`, 可以定义setter:

    ```js
    computed: {
        msg2 : {
            get: function() {},
            set: function() {}
        }
    }
    ```

- 侦听器: 侦听某个属性变化, 如有变动就会被调用:

  ```js
  data: {
      msg: 'test'
  },
  watch: {
  	// 当 msg 变化是被调用    
  	msg: function(newValue, oldValue) {}
  }
  ```

## 2. [VUE实例中的选项/数据](https://cn.vuejs.org/v2/api/#%E9%80%89%E9%A1%B9-%E6%95%B0%E6%8D%AE)

> ==如果在数据对象中使用箭头函数, this的指向将不会按照期望指向Vue实例==, 参看es6, 匿名函数

### 1.data

### 2.computed

> 计算属性, 数据值由计算得到, 注意:==如果计算属性使用箭头函数, 则`this`不会指向这个组件的实例,不过可以通过将例作为函数的第一个参数来访问; `aDouble: vm=>vm.a*2`==

### 3.methods

- 放置事件处理的相关函数;

### 4.watch

> 通过键值对的形式,监控某个数据, 当数据变化时, 调用对应的方法.

## 3.[选项/DOM](https://cn.vuejs.org/v2/api/#%E9%80%89%E9%A1%B9-DOM)

### 1.el

- 提供一个在页面上已存在的DOM元素作为Vue实例的挂载目标.
- 

## 5.[指令](https://cn.vuejs.org/v2/api/#%E6%8C%87%E4%BB%A4)

> 修饰符 (Modifiers) : 是以半角句号 `.` 指明的特殊后缀，用于指出一个指令应该以特殊方式绑定; 

### 1.v-bing, 特性绑定, 简写为`:`

> 动态地绑定一个或多个特性，或一个组件 prop 到表达式;

#### 1.绑定`class`

```html
<!-- 单个绑定 -->
<div :class="oblClassA"></div>
<!-- 对象语法: 由 isActive 值决定 active 是否存在 -->
<div v-bind: class="{active: isActive}"></div>
<!-- 数组语法 -->
<div :class="[classA, classB, 'class1']"></div>
```



- 对象语法: `<div v-bind: class="{active: isActive}"></div>`, 由`isActive`决定`active`是否存在;
  - 也可以将整个`{xx}`对象作为一个参数, `<div v-bind: class="classObject"></div>`, 由决定具体类;
- 数组语法: `<div v-bind:class="[activeClass,  errorClass]"></div>`: 对数组中值进行赋值;

#### 2.绑定其他属性

```html
<img :src="imageSrc">
<!-- 使用js表达式拼接 -->
<img :src="'/path/to/images/' + fileName" 
```

#### 3.绑定prop

```html
<!-- prop 绑定“prop”必须在 my-component 中声明-->
<my-component :prop="someThing"></my-component>
```



### 2.v-if 和 v-show, 条件渲染

> v-if 决定节点是否存在, v-show决定节点是否显示;
>
> v-if 有更高的切换开销, v-show 有更高的初始开销;

#### 1.v-if 

- 根据表达式的值的真假条件渲染元素。

- ==`v-if`==: `<span v-if="isExist"></span>`;
- ==`v-else`==: `<span v-if="type === 'A'">A</span> <span v-else>B</span>`
- ==`v-else-if`==: `<span v-if="type==='A'">A</span> <span v-else-if="type='B'">B</span> <span v-else>C</span>`
- 当同`v-for`共同作用时, `v-for`有更高的优先级; `v-if`将分别作用于每一个`v-for`循环中;

#### 2.v-show

- 根据表达式之真假值，切换元素的 `display` CSS 属性。

- `<div v-show="ok">hello</div>`

### 3.v-for, 列表渲染

> 可作用于: String, Array, Object, number
>
> number: ==循环出 1到指定数;==
>
> Object: ==循环出所有属性值;==

- 列表的循环: `v-for="item in items"` 或者 `v-for="(item, index) in items"`
- 对象的循环: `v-for="value in item"` 或者 `v-for="(value, key) in item"` 或者 ` v-for="(value, key, index) in item"`
- 可以为渲染出的dom增加唯一标识key: `<div v-for="item in items" :key="item.id">

### 4.v-on, 事件处理, 简写为'@'

> 绑定事件监听器。事件类型由参数指定。表达式可以是一个方法的名字(`@click=functionName`)或一个内联语句(`@click=functionNane(xxx, xx), 或 @click=alert('hello')`)，可以跟修饰符(`例如.stop`);
>
> 作用于元素dom可以监听原生DOM事件, 在==自定义元素组件上==可以监听==自定义事件==

- 修饰符: 
  - `.stop`: 停止向上冒泡;
  - `.self`: 本身触发;
  - `.once`: 只触发一次回调;
  - `.left`: 点击左键时触发;
  - `.right`: 点击右键时触发;
- 监听自定义事件:
  - 

### 5. v-model, 表单输入绑定

> 在表单控件或者组件上创建双向绑定

- 可以作用在: `<input>, <select>, <textarea>, components `

## 组件

### 1.组件注册

- 全局注册: `Vue.component('my-component-name', {/*....*/})`: 可以用于任何新创建的Vue跟实例中.
- 局部注册: `var ComponentA={/*....*/}; new Vue({components:{'component-a': ComponentA}})`: components中的每个属性名都是一个组件名称, `ComponentA`为一个js对象, 包含`template, data`等组件所需属性;
- 在模块系统中: `import ComponentA form './ComponentA'`;
- 基础组件的自动化全局注册: 

### 2.Prop

- Prop名如果采用驼峰命名, 在DOM中使用时需要采用短横线分割命名(HTML大小写不敏感)

- 静态传递Prop时, 都默认为String类型, 如果需要传递数字, 布尔等需要绑定, `<blog-post :likes='42'</blog-post>`

- 单向数据流: prop形成了父到子的单向绑定, 可以通过父更新子, 不能通过子更新父;

- prop验证: 通过对象, 指定prop的类型, 

  ```javascript
  props:{
      propA: Number, 
      propB:{
          type: Number, 
          default(){}
     	}, 
      propC:{
          validator(){}
      }
  }
  ```

### 3.自定义事件

- 跟组件名和prop不同, 不会将驼峰命名转换为短横线分割命名, 并且由于HTML大小写不敏感, 所以`v-on:myEvent 转换为 v-on:myevent`导致事件不能被监听, 推荐使用 短横线命名;

- 通过`this.$emit('my-event')`: 
- `.sync`

## 命名规则

- 自定义组件名: 字母全小写且必须包含一个连字符; 当使用驼峰命名时例如(MyComponentNmae), 引用时可以引用`<my-component-name> 也可 <MyComponentName>`;
- prop: 
- 自定义事件名: 短横线命名, 