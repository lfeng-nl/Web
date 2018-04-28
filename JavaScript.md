## 1.基础概念

- JavaScript 和 ECMAScript：
  - 完整的JavaScript 实现应由：ECMAScript、DOM、BOM 三部分组成；
  - ECMAScript  ：实现标准规定的各个方面内容的语言的描述（语法，类型，语句...）；
  - DOM ：文档对象模型，针对 XML 但经过扩展用于 HTML 的应用程序接口；
  - BOM ：浏览器对象模型，访问和操作浏览器窗口；

### 1.数据类型

> ECMAScript共有5种简单数据类型和一种复杂数据类型，

- Undefined 类型：只有一个值，`undefined`，表示变量使用`var`声明但未对其加以初始化；
- Null 类型：只有一个值，`null`，表示一个空对象指针；
- Boolean 类型：只有两个字面量，`true、false`；
- Number 类型：
- String 类型：
- Object 类型：对象类型，由键值组成的无序集合，
  - 创建：`var o = new Object() 或 var o = {}`；
  - ​

### 2.引用类型

> 在js中，**引用类型**是一种数据结构，用于将数据和功能组织在一起；类似于通常所说的类，但并不是相同的概念，对象为引用类型的实例。引用类型也称为 **对象定义**

- Object类型：使用较多的引用类型，主要用于存储数据（类似python字典）

  - 创建及使用：

    ```javascript
    /* 第一种创建方式 */
    var person = {
        name = 'xxx';
        age = 20;
    }

    /* 第二种创建方式 */
    var person = new Object();
    person.name = 'xxx';
    person.age = 20;

    console.log(person.name);               // 可以使用 点 取得属性值
    console.log(person['name']);            // 方括号取值，优点是可以通过变量取值
    ```

- `Array`类型：

- `Date`类型：

- `RegExp`类型：

- `Function`类型：

- 基本包装类型：`String, Boolean, Number`:

- 其他：

  - Global对象：不属于任何其他对象的属性和方法，最终都是Global对象的属性和方法；终极兜底对象；
  - 所有全局作用域中声明的变量、函数都会映射为` window`对象的属性和方法；
  - Math对象：

### 3.面向对象

> 类：在其他面向对象语言中，类是一个可以创建任意多个具有相同属性和方法的一种特殊类型。
>
> JS中没有类的概念，对象定义为：无序组合，其属性可以包含基本值，对象或者函数；

## 标准对象

### 1.JSON

- 序列化：将对象转为JSON字符串`JSON.stringify(xxxx)` ；
- 反序列化：将JSON字符串转为JavaScript对象 `JSON.parse(xxx)` ；

## BOM

> BOM 的核心对象是`window `,它表示浏览器的一个实例；它既是通过 JavaScript 访问浏览器窗口的一个接口，又是 ECMAScript 规定的 Global 对象。

- 所有全局作用域中声明的变量、函数都会映射为` window`对象的属性和方法；
- 如果页面中包含框架（html的`frame`标签），则每个框架都拥有自己的window对象，并且保存在`frames `集合中，

### 1.location对象

> 提供当前窗口中加载的文档有关的信息；既是window对象的属性，也是document对象的属性；访问时可以用`window.location`也可以用`location`；

- 对象属性：

  - `host`：设置或返回主机名和当前 URL 的端口号；
  - `href`：设置或返回完整的URL；==设置后会直接跳转到新的URL上==；
  - `search`：设置或返回从问号（？）开始的URL（查询部分）；
  - `host`：设置或返回主机名和当前 URL 的端口号。

- 对象方法：

  - `reload()`：重新加载当前文档；

  - `assign()`：打开新的url并在浏览器历史记录中生成一条记录；同设置`location.href`属性效果相同（常用）；

  - `replace()`：导航到相应的url，但不会在历史记录中生成；

    ​

### 2.navigatior对象

> 提供浏览器及相关环境信息

- `userAgent()`：浏览器用户代理字符串，声明了浏览器用于HTTP情求的用户代理头的值；可用于判断移动端还是PC端，浏览器类别；
- `systemLanguage()`：返回OS使用的默认语言；

### 3.间歇调用和超时调用

js为单线程语言，允许设置超时或间歇调用，使代码在特定时刻执行；

- 超时：`setTimeout(函数名，超时时间)`，超过指定毫秒数后，指定代码被执行；

  - `setTimeout()` 会返回一个数值`id `，可以用` clearTimeout(id)`来消除超时调用；

  - ```js
    timeoutId = setTimeout(function(){...}, 1000);     // `1000ms后执行匿名函数
    clearTimeout(id);									// 清除超时调用
    ```

- 间歇：`setInterval(函数名，间歇时间) `,每隔间隔时间，函数被执行；

  - `setInterval()` 会返回一个数值`id `，可以用` clearInterval(id)`来消除间隔调用；
  - 应尽量避免使用间歇调用；

###4.系统对话框

- `alert() `：生成警告，仅向用户显示信息；
- ` confirm()`：确认对话框，将用户选择信息返回；
- `prompt()`：提示框，提示用户输入一些文本；

## DOM

> 文档对象模型，是针对HTML和XML文档的一个API。DOM描绘了一个层次的节点树，允许开发人员添加，移除和修改页面的某一部分。
>
> document 对象是HTMLDocument的一个实例，表示整个HTML页面；

###1.节点层次：

- 所有标记页面表现为一个特定节点为根节点的树形结构（HTML，根节点为Document，而非html 元素标签）；
- `nodeType`：
  - 元素标签类型（1）
  - 属性类型（2）
  - 文本类型（3）
  - 注释（8）
  - Document,根节点（9）
- `nodeName` ：不同类型的节点，名称意义不同
  - 元素节点的 `nodeName `是标签名称（大写）
  - 属性节点的 `nodeName` 是属性名称
  - 文本节点的 `nodeName `永远是 `#text `
  - 文档节点的 `nodeName` 永远是 `#document `
- `nodeValue` ：
  - 对于文本节点`nodeValue`是文本信息；
  - 对于属性节点`nodeValue`是属性值；
  - 对于元素节点`nodeValue`始终是null；
- 节点关系：
  - `childNodes`属性，保存着NodeList对象，NodeList用于保存一组有序节点；可以向数组一样访问其中元素，基于DOM结构动态执行查询结果。
  - `parentNode`属性，指向其父节点；
  - `previousSibling`属性，指向前一个同胞节点；
  - `nextSibling`属性，指向后一个同胞节点；
- 增加或删除节点
  - `document.createElement('div')`：创建一个元素节点，参数为元素的节点名;
  - `document.createTextNode('xxx') `：创建文本节点，参数为需要插入节点中的文本；
  - `somenode.appendChild(newNode)`：用于向`somenode 的 childNodes`列表后添加一个节点；
  - `somenode.cloneNode()`：创建调用这个方法的节点的一个与`somenode `完全相同的副本;
- document
  - `document.body`属性：指向`<body>`元素节点；
  - `document.doctype`属性：指向`<!DOCTYPE>`标签；
  - `document.title`属性：该页面标题；
  - `document.URL`属性：该页面完整的URL，例如`http://www.wrox.com/WileyCDA/`；
  - `document.body`属性：改页面的域名，例如`www.wrox.com`；

> tips:对于`http://mail.163.com/index.html`
>
> http：指协议；
>
> mail：服务器名；
>
> 163.com：域名，用于定位网站的独一无二的名字；
>
> http://mail.163.com/index.html：url，统一资源定位符；

###2.Element元素标签类型

- 查找
  - `document.getElementById()`：通过id查找节点；
  - `document.getElementsByTagName()`：通过标签名查找节点，返回一个nodeList；
  - `document.getElementsByName()`：通过name查找节点，一般用于选定一组节点；
- 重要属性
  - `id`：元素的id值；
  - `className`：元素的类名；
  - `attributes`：Attr节点的动态集合；
- 重要方法
  - `getAttribute('xx')`：获取指定属性的值；
  - `setAttribute('xxx', 'xxx')`：设置指定属性指定值；