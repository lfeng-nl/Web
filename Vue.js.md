## 1.Vue基础

### 1.实例

```js
var vm = new Vue({
    el: "#n_id",
    data: {
        name: 'xxx'
    },
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
- if: `<p v-if="seen">通过seen的值决定是否存在此条标签</p>`, 
- for: `<li v-for="todo in todos">{{ todo }}</li>`
- 修饰符: 以`.`指明的特殊后缀, 用于指出一个指令应该以特殊方式绑定;
- 缩写: `v-bind --> : ;  v-on --> @`

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
  	msg: function() {}
  }
  ```

### 4.Class 和 Style绑定

- `<span v-bind:class="{active: isActive}" class="nomal"> xxx </span>` : active类是否存在决定于`isActive`的bool值;
- 绑定多个类: `<span v-bind:class="[data1, data2, data3]"> xxx </span>`

### 5.v-if 和 v-show

> v-if 决定节点是否存在, v-show决定节点是否显示

- `v-if: <span v-if="isExist"></span>`;
- `v-if="type === 'A'" .... v-else`
- `v-if ... v-else-if ... v-else ...`

### 6.v-for

- 列表的循环: `v-for="item in items"` 或者 `v-for="(item, index) in items"`

- 对象的循环: `v-for="value in item"` 或者 `v-for="(value, key) in item"`
- 