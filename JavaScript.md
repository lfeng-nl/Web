

## 1.基础概念

- JavaScript 和 ECMAScript：
  - 完整的JavaScript 实现应由：ECMAScript、DOM、BOM 三部分组成；
  - ECMAScript  ：实现标准规定的各个方面内容的语言的描述（语法，类型，语句...）；
  - DOM ：文档对象模型，针对 XML 但经过扩展用于 HTML 的应用程序接口；将整个页面映射为一个多层节点结构；
  - BOM ：浏览器对象模型，访问和操作浏览器窗口；使用BOM可以控制浏览器显示的页面以外的部分；

### 1.基本数据类型

> ECMAScript共有5种基本数据类型（Undefined, Null, Boolean, Number, String）和一种复杂数据类型(Object)，使用`typeof`可以查看对象的类型；
>
> 基本类型为什么可以有属性和方法：通过包装类实现；

- Undefined 类型：只有一个值，`undefined`，表示变量使用`var`声明但未对其加以初始化；
- Null 类型：只有一个值，`null`，表示一个空对象指针；如果对象声明用于将来保存对象，那么最好将该变量初始化为`null`;
- Boolean 类型：只有两个字面量，`true、false`；
- Number 类型：
  - 可以赋值为10进制，0开头的八进制，0x开头的十六进制的整数；
  - 可以赋值为浮点数；
  - 可表示值范围：Number.MAX_VALUE~Number.MIN_VALUE；
  - `-Infinity, +Infinity`：正、负无穷；
  - `NaN`：非数值；类型属于Number，一个特殊值，用于表示本来要返回数值的操作数未返回的情况；
    - 1.与任何值都不相等，包括自身；
    - 2.与任何数的计算都为NaN；
    - 3.可通过`isNaN( )`判断是否为“数值”，能否“不是数值”，注意！！！如果能转为数值，则为false；
- String 类型：
- `typeof `和`instanceof`
  - `typeof a`：变量a的类型；一般只返回几个类型：`string, number, boolean, function, undefined`；
  - `a instanceof constructor`：测试原型和实例的关系；

### 2.符号

> JavaScript符号基本同C相同；

- 不同点：
  - 1.`>>`有符号右移（可简单认为，符号位保留，然后移动）；`>>>` 无符号右移；（符号位参与移动，原位置补0）（总得到正数）；
  - 2.`===`全等和`==`相等：例如`'55'==55`会返回true，`'55'===55`会返回false；相等如果类型不同会按照相应规则做类型转换，而全等不做类型转换；3.`!==`不全等和`!=`不相等：

- 条件操作符号：`variable = booolean_expression ? true_value : false_value;`

### 3.语句

> 大部分同c相同：if...else..., while(), for(), break, continue, switch()...case:

- `for-in`语句：`for(x in l){ .....; }
  - 用于枚举对象的==属性== ；
  - 旧版本`for-in`用于值为`null, undefined`的对象会抛出异常(ES5之后的版本不会）；
- `for-of`语句：`for( x of l){ ... ; }
  - 用于遍历数组，取出值；
  - ES6 引入的特性，不能作用于普通对象；
- `label`语句：可以在代码中添加标签；`start: ...;`
- `with`语句：向代码的作用域设置到一个特定的对象中：`with (expression) statement;`(不建议使用)；

### 4.函数

- 没有重载：JavaScript 函数不能重载，如果定义了多个函数，那么函数名属于后定义的函数；
- `JavaScript`中的函数定义并未指定函数形参的类型，函数调用也不会对传入的实参做任何检查；

### 5.变量

- 变量可以包含两种不同数据类型的值：基本类型值和引用类型值；
  - 基本类型值：5种基本数据类型，按值访问；
  - 引用类型值：保存在内存种的对象，与其他语言不同，JavaScript不允许直接访问内存种的位置，所以，引用类型的值是按引用访问；
  - 通过变量赋值和函数传递参数时，将体现出差异；

### 6.执行环境

#### i.作用域

- JavaScript没有块级作用域；例如

  - ```javascript
    if （true) {
        var color = 'blue';
    }
    console.log(color);
    ```

- 变量提升：当变量被声明时，声明会提升到他所在函数的顶部；

  - JS引擎在进入作用域时会对代码分两轮处理。第一轮，初始化变量，第二轮，执行代码；

- js会自动向上层搜索，直到到全局作用域；应为js有`var`，所以能够知道到底是新声明还是调用；这同`python`略有不同；python需要改变其他作用域变量时需要`global`或`nonlocal`声明；

#### ii.执行环境

- 每当函数被调用，就会产生一个新的==执行环境==；
- 属于执行环境部分的变量和函数，被保存在==执行环境变量==中


## 2.引用类型和面向对象

> 在js中，**引用类型**是一种数据结构，用于将数据和功能组织在一起；类似于通常所说的类，但并不是相同的概念，对象为引用类型的实例。引用类型也称为 **对象定义**;
>
> 同其他面向对象语言的类的区别：**类**通常用于创建一类具有相同属性、方法的对象；

### 1.常用引用类型

- Object类型：使用较多的引用类型，主要用于存储数据（类似python字典）

  - 创建及使用：

    ```javascript
    /* 第一种创建方式 */
    var person = {
        name : 'xxx';
        age : 20;
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

  - 创建时如果无参数则自动获取当前时间，如果根据特定日期和时间创建，需要传入毫秒数（UTC）；

- `RegExp`类型：正则表达式；

- `Function`类型：函数是对象，函数名是指针；

  - 函数名本身就是变量，所以函数也可以作为值来使用，可以将函数作为参数传递给另一个函数；
  - ==函数内部属性==：在函数内部，有两个特殊的对象，`arguments`和`this`；在函数内可做变量使用；
    - `arguments：`包含传入的参数，
    - `this`：函数据以执行的环境对象，在网页全局作用域种调用函数时，this对象向就是window；
  - 函数本身也是对象，所以函数也具有属相和方法：
    - `length`：函数希望接受的命名参数的个数；
    - `prototype`：原型属性，指针，指向一个对象；该对象是包含可以由特定类型的所有实例共享的属性和方法；
    - `apply(), call()`方法：可以在特定的作用域中调用函数（可以把传递`this`参数）；

- 基本包装类型：为便于操作基本类型值，JavaScript还提供了3 个特殊的引用类型：`String, Boolean, Number`；当读取一个基本类型值的时候，后台就会创建一个对用的基本包装类型的对象，从而能够嗲用一个方法来操作这些数据；

  - 基本类型表达的应该仅仅是内存数据（值）；
  - 当调用基本类型相关的方法时，后台会自动完成：1.创建相关包装类型实例，2.在实例上调用指定方法，3.销毁实例；
  - 可以通过：`var stringObject = new String("hello world");`创建`String`类型；

- 其他：

  - `Global对象`：不属于任何其他对象的属性和方法，最终都是Global对象的属性和方法；终极兜底对象；
  - `window对象`：所有全局作用域中声明的变量、函数都会映射为` window`对象的属性和方法；
  - `Math`对象：

### 2.面向对象

> 类：在其他面向对象语言中，类是一个可以创建任意多个具有相同属性和方法的一种特殊类型。
>
> JS中对象的定义：无序属性的组合，其属性可以包含基本值、对象或者函数；
>
> 每个对象都是基于一个引用类型创建的；

- 注意：==原型中的内容只有一份，所有实例通过指针指向，类似c++中静态成员==

#### 1.创建对象

>Object通常只用于构造单个对象；如果需要向其他语言一样创造特殊的构造函数这需要使用特殊的方法；

- 属性类型:
  - 数据属性：包含一个数据值的位置；在这个位置可以读取和写入值；
  - 访问器属性：不包含数据，但包含一对`getter`和`setter`函数，同个这两个函数处理数据；

- JS有以下的几种创建构造对象方式：（常用的是：构造函数模式+原型模式）

  - 工厂模式：可以方便构造同类型对象，但无法解决对象识别；

    ```javascript
    function createPerson(name, age, job) {
        var o = new Object();
        o.name = name;
        o.age = age;
        o.job = job;
        return o;
    }
    ```

  - 构造函数：

    ```javascript
    function Person(name, age, job) {
        this.name = name;
        this.age = age;
        this.job = job;
    }
    
    // 使用方法
    var p = new Person(name, age, job);
    ```

    - 缺点：每个方法都要在每个实例上重新创建一遍；==虽然可以通过定义全局函数来解决，但违背了封装的宗旨==；

#### 2.原型模式：

- > 每个创建的==函数==都有一个==`prototype`==的属性，这个属性是一个指针，指向==原型对象==，而这个对象的用途可以由包含可以由所有实例共享的属性和方法；通俗讲：每个函数都有`prototype`属性，`prototype`指向一个对象，该对象的属性和方法被所有实例共享；
  >
  > ==实例会有一个`__proto__`的指针==指向原型对象；
  >
  > ==原型对象==包含一个==`constructor`属性==，指向构造函数；
  >
  > ![prototype](D:\GitHub\Web\image\prototype.png)

- 原型链的搜索机制：当以读取模式访问一个实例属性时，首先会在实例中搜索该属性，如果没有找到该属性，则会继续搜索实例的原型；

- 

  ```javascript
  function Person() {
  }
  Person.protorype = {
      name = 'xxx';
  	age = 26;
      sayname: function() {
      	alert(this.name);
  	}
  
  var p1 = new Person();
  ```

- 原理：通过`protorype`使所有的实例共享属性和方法；但却不能通过实例重写原型中的值；也就是说，实例改写

- 值只会影响自身；![](D:\GitHub\Web\image\prototype重写属性.png)

- `hasOwnProperty()`可以检测属性是存在于实例中（true），还是存在于原型中（false)；

- 原型具有动态性；

- 原生的引用类型，都是采用这种模式创建的，==都在其构造函数的原型上定义了方法==；   

- ==构造函数模式+原型模式== 最为常见的方式

  - 构造函数模式用于定义实例属性；
  - 原型模式用于定义方法和共享属性；

#### 3.继承

- 原型链：构造函数都有一个原型对象（`prototype`），而实例都有一个指向原型对象的内部指针(`__proto__`)；如果让一个构造函数的原型对象等于一个另一个类型的实例，此时，原型对象将包含指向另一个原型对象的指针，这就是原型链；

- js依靠原型链实现继承，`SubType.prototype  = new SuperType(); `

- 问题：无法向超类中传参数；

- 解决方法：借用构造函数：

  - ```javascript
    function SubType() {
        // 构造函数 --> 在其内部对this增加属性，通过父类的call()方法，传入子类的`this`，相当于直接对子类增加属性；
        SupperType.call(this);  
    }
    ```

- 组合式继承：应用最广泛

  - ```javascript
    function SubType() {
        // 1.可以传参，2.直接在this中增加属性；
        SupperType.call(this);  
    }
    // 继承方法，（属性也会在prototype中在次包含，但是会被this中的覆盖）
    SubType.prototype = new SupperType();
    
    ```

- 原型式继承

## 3.函数表达式

- 匿名函数：`function`关键字后没有标识符，也叫`lambda`函数；

- 立即调用的函数表达式 （自执行的匿名函数 ）：创建一个匿名函数并立刻执行；

  ```javascript
  (function(x) {
      console.log(x);
  })('hello world!');
  ```

### 1.闭包：

> 闭包：阻止垃圾回收器将变量从内存中移除，使在创建变量的执行环境的外部能够访问该变量；
>
> 创建闭包的常见方式，就是在一个函数内部创建另一个函数；
>
> 实现原理：一般函数执行完毕，局部活动对象就会被销毁，内存中仅保留全局作用域；但是闭包：内部函数会将__包含函数的活动对象__添加到它的作用域链中；闭包就可以访问包含函数的所有变量，并且由于匿名函数的引用，这些对象也不会销毁；（十分类似C语言函数内部用`static`声明；）

- 闭包包围的是变量空间，而非值；

### 2.call 方法

- 个人理解：当函数默认调用时，`this`指向`window`，当用call方法调用，可以传入指定的运行环境，`this`指向传入对象；

- `function.call(thisArg, arg1, arg2, ...)`：给定this值，和一些参数；

  ```python
  function Product(name, price) {
      this.name = name;
      this.price = price;
  }
  
  Product.call(thisObject, name, price);
  ```

  > 关于new：例如上述例子中，如果`var p = new Product('name', price)` 则生成了一个具有name，price属性的对象，new做了关键性的几部：1.创建一个obj`var obj = {}`；2.将`__proto__` 指向 `Product.prototype`（原型对象）；3.调用`Product.call()`，传入`obj`;

## 4.BOM

> BOM 的核心对象是`window `,它表示浏览器的一个实例；它既是通过 JavaScript 访问浏览器窗口的一个接口，又是 ECMAScript 规定的 Global 对象。
>
> 重要点：location.href 跳转，间歇调用和超时调用；

- 所有全局作用域中声明的变量、函数都会映射为` window`对象的属性和方法；
- 如果页面中包含框架（html的`frame`标签），则每个框架都拥有自己的window对象，并且保存在`frames `集合中;
- `top`对象始终指向最高（最外层）的框架（top 等于最外层框架的window)，也就是浏览器窗口；可以用`top.frames[0]`指向其他frame；

### 1.location对象

> 提供当前窗口中加载的文档有关的信息；既是window对象的属性，也是document对象的属性；访问时可以用`window.location`也可以用`location`；
>
> 比较重要的就是通过`location.href `进行跳转、超时调用

- 对象属性：

  - `host`：设置或返回主机名和当前 URL 的端口号；
  - `href`：设置或返回完整的URL；==设置后会直接跳转到新的URL上==；
  - `search`：设置或返回从问号（？）开始的URL（查询部分）；
  - `host`：设置或返回主机名和当前 URL 的端口号。

- 对象方法：

  - `reload()`：重新加载当前文档；
  - `assign()`：打开新的url并在浏览器历史记录中生成一条记录；；
    - 同设置`location.href`属性（常用）或设置`winddow.location`效果相同
  - `replace()`：导航到相应的url，但不会在历史记录中生成；


### 2.navigatior对象(导航)

> 用于识别客户端浏览器，

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

### 4.系统对话框

- `alert() `：生成警告，仅向用户显示信息；
- ` confirm()`：确认对话框，将用户选择信息返回；
- `prompt()`：提示框，提示用户输入一些文本；

## 5.DOM

> 文档对象模型，是针对HTML和XML文档的一个API。DOM描绘了一个层次的节点树，允许开发人员添加，移除和修改页面的某一部分。
>
> ==document== 对象是HTMLDocument的一个实例，表示整个HTML页面；

### 1.节点层次：

- 所有标记页面表现为一个特定节点为根节点的树形结构；HTML，根节点为`Document`，而非html 元素标签；html标签为文档元素；
- ==元素节点向下包括：属性节点、文本节点、其他元素节点.==..
- 所有的节点类型，JS中以`Node`类型实现；每个节点由`nodeType`定义其属性；
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
  - `childNodes`属性，保存着NodeList对象，NodeList用于保存一组有序节点；可以向数组一样访问其中元素，基于DOM结构动态执行查询结果。还有`firstChild、lastChild`指向第一个、最后一个子节点；
  - `parentNode`属性，指向其父节点；
  - `previousSibling`属性，指向前一个兄弟节点；
  - `nextSibling`属性，指向后一个兄弟节点；
- 通过关系操作节点：
  - `appendChild()`，向子节点末尾插入一个节点；
  - `insertBefore()`，向指定节点前插入一个节点；与之成为兄弟节点；
  - `replaceChild()`，替换子节点；

### 2.document 节点

> `document` 对象是`HTMLDocument` 的一个实例，表示整个HTML页面；`document`对象是`window`对象的一个属性；

- 提供文档信息
  - `document.body`属性：指向`<body>`元素节点；
  - `document.doctype`属性：指向`<!DOCTYPE>`标签；
  - `document.title`属性：该页面标题；
  - `document.URL`属性：该页面完整的URL，例如`http://www.wrox.com/WileyCDA/`；
  - `document.body`属性：改页面的域名，例如`www.wrox.com`；
- 节点创建删除
  - `document.createElement('div')`：创建一个元素节点，参数为元素的节点名;
  - `document.createTextNode('xxx') `：创建文本节点，参数为需要插入节点中的文本；
- 节点的查找
  - `document.getElementById()`：通过id查找节点；
  - `document.getElementsByTagName()`：通过标签名查找节点，返回一个nodeList；
  - `document.getElementsByName()`：通过name查找节点，一般用于选定一组节点；

> tips:对于`http://mail.163.com/index.html`
>
> http：指协议；
>
> mail：服务器名；
>
> 163.com：域名，用于定位网站的独一无二的名字；
>
> http://mail.163.com/index.html：url，统一资源定位符；

### 3.Element 类型 节点

- 重要属性
  - `id`：获取或设置元素的id值；
  - `className`：获取或设置元素的类名；
  - `innerText`：内部文本信息，（注意，可能是子节点的文本信息）；
  - `innerHTML`：内部HTML信息；
  - `attributes`：属性节点的动态集合；
- 重要方法
  - `getAttribute('xx')`：获取指定属性的值；
  - `setAttribute('xxx', 'xxx')`：设置指定属性指定值；
  - `removeAttribute('xxx')`：删除指定属性；

### 4.Text 节点

### 5.Attr节点

- 不太会直接访问属性节点，都是通过`getAttribute(), setAttribute, removerAttribute`等方法操作；

## 6.事件

- 事件冒泡：事件开始由最具体的元素（文档中嵌套层次最深的那个节点）接收；然后逐级向上传播到不具体的节点；
- 事件：用户或浏览器自身执行的某种动作，如`click, load, mouseover`； 响应某个事件的函数就叫事件处理程序；
- 在事件处理程序中，通过`this`访问元素的任何属性和方法；

### 1.事件的种类

- UI事件
  - `load`：当页面完全加载后会触发；
  - `resize`：浏览器窗口调整大小时触发；
  - `scroll`：滚动；

- 焦点事件
  - `blur`：元素失去焦点时触发；
  - `focus`：元素获得焦点时触发；

- 鼠标与滚轮事件

  - `click`：单击鼠标按钮时触发；

  - `mousemove`：鼠标指针在元素内部移动时重复的触发；

  - `mouseenter`：鼠标光标从元素==外部==首次移动到元素范围内时触发；

  - `mouseleave`：位于元素上方的鼠标移动到元素范围外时触发；

  - `mouseleave`：位于元素上方的鼠标移动到另外一个元素时触发；

  - `load`：当页面完全加载后会触发；

## 7.ES6

### 1.局部变量和常量

- `let`: 创建块级作用域变量;
- `const`: 声明常量;

### 2.箭头函数

- `(参数1, 参数2, 参数3) => { 函数声明 }`: 

### 3.函数参数默认值

### 4`for...of VS for...in`

- `for...of`: 遍历迭代器;
- `for...in`: 遍历对象属性;

### 5.Spread/Rest操作符

- `let a=[1,2,3]; foo(...a)`: 会将迭代器展开, 元素作为参数传递到函数中;
- `(...a)=>{console.log(a)}`: 将传入的操作合并为一个可迭代对象;

### 6.Module

> 模块功能主要由两个命令构成: export和import, export用于规定模块的对外接口; import用于输入其他模块提供的功能;

- `export `: 输出变量

  - ```javascript
    // 方式1
    export var firstName = 'liu'
    
    // 方式2
    var firstName = 'liu'
    export {firstName}
    
    ```

- `import`: 加载模块

  - ```javascript
    import {firstName} from "./profile.js"
    ```

  - 通过import命令出入的变量都是只读;

  - `import`命令会被JavaScript引擎静态分析, 先于模块内的其他语句执行;

- `export default`: 为模块指定默认输出; 其他模块加载该模块时, `import`命令可以指定任意名称, 且也不需要大括号;

  - 一个模块只能用一个默认输出;
  - `export default`就是输出一个叫做`default`的变量或方法, 等同于`export {xx as default}`

- 

### 8.console

- `console.log()`: 普通输出;
- `console.time/timeEnd`: 计时;
- `console.table(data)`: 以表格形式输出;
- `console.assert(isDebug, 'log')`: 断言, 根据isDebug进行输出;

## 标准对象

### 1.JSON

- 序列化：将`JavaScript`对象转为`JSON`字符串：`JSON.stringify(xxxx)` ；
- 反序列化：将`JSON`字符串转为`JavaScript`对象： `JSON.parse(xxx)` ；

### 2.localStroage，sessionStorage

> HTML5中，新加入了一个localStorage特性，主要用来作为本地存储，解决了cookie存储空间（每条cookie 4K）不足的问题，一般浏览器支持5M大小的空间；
>
> localStorage与sessionStorage的唯一一点区别就是localStorage属于永久性存储，而sessionStorage属于当会话结束的时候，sessionStorage中的键值对会被清空 

- `localStorage.getItem()`：读取值；
- `localStorage.setItem()`：存储值；
- `localStorage.clear()`：清除所有；
- `localStorage.removeItem()`：清除指定；

## 日常开发

- 调试JS时无法找到动态加载的JS源文件：在文件开头或结尾加上`//@ sourceURL=xxx.js`，就可以在no domain中找到需要调试的文件；