- [URL href 和 src 的区分](https://segmentfault.com/a/1190000002877022)
  - url:
  - href：Hypertext Reference，仅指向网络资源所在位置，建立和当前元素或当前文档之间的链接；页面解析不会暂停；如 `<a> `标签；样式表的 `<link>` 表示需要外部资源，`href` 指向资源所在位置；
  - src：sourse缩写，指向外部资源位置，指向的内容会嵌入到文档中当前标签所在位置；当浏览器解析到当前元素时，会暂停其他资源的处理；可以理解为需要资源对该标签进行填充；

## 1.基本概念

> ```html
> <!DOCTYPE HTML>
> <html>
>     <hand>
>         <title>Example</title>
>         <!-- 其他元数据 -->
>     </hand>
>     <body>
>     </body>
> </html>
> ```
>
> html文档结构

### 1.元素

```html
<span>这就是一个元素</span>
```

- 元素不区分大小写
- 元素关系: 父元素, 子元素, 后代元素,兄弟元素等..
- 元素类型:
  - 元数据元素: 用来向浏览器提供文档的一些信息, 如标题, 编码等;放在`<hand></hand>`标签中; 
  - 流元素: 
  - 短语元素:

### 2.属性

- 元素属性: 属性只能出现在开始标签上, 
  - 属性一般由属性名和属性值构成: `<span class="test">属性</span>`
  - 布尔属性: 不需要设定一个值, 只需将属性名添加到元素中即可, 例如`<input disabled/>`, 
    - 当只写属性名时:`disabled 等同于disabled="true"`;
    - 不写该属性代表false
  - 属性值两边可以是单引号, 也可以是双引号, H5也可省略引号,但不能包含引起特殊意义的字符;
- 全局属性: h5增加概念, 所有元素都可配置
  - `class`: 类
  - `contenteditable`: 使用户可以修改其上内容; 
  - `draggable`: 可以拖放;
  - `hidden`: 隐藏; 布尔属性,
  - `id`: 分配唯一标识; 

## 2.元数据元素

- `title`: 设置标题;
- `base`: 设置基准`URL`, 如果不设置, 已当前页面为基准; `<base href="/test/"/>`
- `mate`: 用来定义文档的各种元数据
  1. `name="key" content="value"`: name用来表示元数据的类型, `content`用来提供值;
  2. `charset="utf-8"`: 字符编码., 
  3. `http-equiv="refresh" conten="5"`: 定时刷新页面

- `style`: 定义样式;
  - `type`: 定义样式类型, 浏览器只支持CSS样式 ,所以 ,值始终为`text/css`
  - `media`: 用来表明文档在什么情况下应该使用该元素中定义的样式
    - `screen`: 计算机显示屏幕, `print`: 打印,打印预览 
- `link`: 指定外部资源(常用语CSS样式表)
  - `rel`: 说明文档与所关联资源的关系类型;
    - `icon`: 指定页面的网页标识;
  - `type`: 关联资源的类型, text/css, image/x-icon
  - `href`: 指向资源的url,
- `script`: 使用脚本元素:
  - `type`: 脚本类型, JavaScript类型可以省略;
  - `src`: 指定外部脚本的url, 

## 3.重点元素标签

- `<a />`: 超链接
  - `href`: a元素所指定元素的url, `href="#id"`锚点, 跳转到内部指定id上;
  - `target`: 指定连接资源显示;

- `<span></span>`: 本身无任何含义, 用于将全局属性应用到一段内容上; 

- `<p></p>`: 段落,

- `<div></div>`: 本身不具有任何意义; 

- `<ul></ul>`: 无序列表;

  - `<li></li>`: 列表中的项目;

### 文字相关元素

- `<b></b>`: 标记一段文字, 但并不代表特别强调或重要性; 
- `<i></i>`: 表示这段文字与周围内容有本质区别;
- `<s></s>`: 表示一段文字不准确或校正;
- `<sub></sub>, <sup></sup>`: 下标或上标;
- `<wbr>`: 建议换行;

## 4.H5中增加的文档结构性标签

- `<article></article>`:  表示页面中的一块与上下文不相关的独立内容, 可以独自被外部引用, 可以是一篇博客或报刊, 一篇用户评论或插件, `article`元素通常会有自己的标题, 注脚等;

- `<section></section>`: 表示页面中的一个内容区块,例如章节,页眉,也脚或页面中的其他部分;

  - `section`作用是对页面上的内容进行分块,或者说对文章进行分段;
  - `article`强调的是独立, `section`强调的是分块或分段;

- `<header></header>`: 表示页面或文章或一节的首部, 可包含各种适合出现在首部的东西, 包括刊头或徽标;

  - `<hgroup></hgroup>`: 将标题和子标题进行分组,

- `<footer></footer>`: 表示页面或文章或一节的尾部.

  ```html
  <!-- 例子 -->
  <body>
      <header></header>
      <session>
          <header></header>
          <session></session>
      </session>
      <footer></footer>
  </body>
  ```

- `<nav></nav>`: 表示整个页面中的导航链接;
- `<aside></aside>`: 当前页面或文章的附属信息部分,

## 5.表单标签

- `<form></form>`: 表单
  - `action="/test/tset"`: 应该将数据发送到的地方;
  - `method="post"`: 表单提交方式;
  - `name`: 可用于css选择, 不发送到浏览器;
- `<input></input>`: 
  - `autofocus`: 自动聚焦, 表单显示的时候就聚焦于某个input元素; 
  - `disabled`: 禁用;
  - `type`: 类型, 
  - `placeholder`: 用户出入提示
- `<button></button>`: 按钮
  - `type`: submit, 提交表单(默认); reset, 重置表单; button, 仅为一个按钮, 
  - `form`: h5, 通过form与任意表单挂钩;
- `<select></select>`: 下拉框;
- `<label></label>`: 

## 6.本地存储

> h5新增, 改进cookies存储机制的缺点, 使用它可以在客户端本地建立一个数据库
>
> localStorage: 将数据保存在客户端本地的硬件设备,即使浏览器被关闭, 该数据仍然存在, 下次打开浏览器可以继续使用;
>
> sessionStorage: 将数据保存在session对象中, session对象可以用来保存一段时间内所要保存的任何数据;关闭浏览器后数据消失;

### 1.localStorage

- 保存数据: localStorage.setItem(key, value);
- 读取数据: localStorage.getItem(key)

### 2.sessionStorage

- 保存数据: sessionStorage.setItem(key, value);
- 读取数据: sessionStrong.getItem(key);

## 7.离线应用

> 1.用户可离线访问应用，这对于无法随时保持联网状态的移动终端用户来说尤其重要
>
> 2.用户访问本地的缓存文件，通常意味着更快的访问速度
>
> 3.仅仅加载被修改过的资源，避免同一资源对服务器多次的请求，大大降低了对服务器的访问压力
>
>  Web应用程序的本地缓存是通过每个页面的manifest文件来管理的

- manifest: 文本文件,列举需要被缓存或不需要缓存的文件名,以及资源文件的访问路径; 第一行必须是`CACHE MANIFEST`
- html中引入: `<html manifest="demo.manifest"></html>` 
- 浏览器请求过程: 
  1.  请求网页;
  2. 返回index.html;
  3. 浏览器解析, 请求页面上所有资源文件, 包括HTML文件, 图像, CSS文件等等, 以及manifest文件;
  4. 服务器返回所有资源文件,
  5. 浏览器处理manifest文件, ==请求manifest中所有要求本地缓存的文件, 包括index.html,这是一个重复请求==,
  6. 服务器缓存所有本地缓存文件;
  7. 浏览器对本地缓存进行更新, 出发事件, 通知本地缓存被更新;
- 再次打开本地缓存的页面:
  - 有本地缓存, 浏览器使用给本地缓存;
  - 请求manifest文件;
  - 有更新, 请求更新的资源, 

## 8.通信API

### 1.跨文档消息传输

> HTML5 提供了在网页文档之间相互接收和发送信息的功能, 使用这个功能, 只要获取到网页所在窗口对象的实例, 就可以使用该实例向目标文档发送消息

- `window.addEventListener("message", function(env){...}, false)`: 监控窗口的message事件;
- `otherWindow.postMessage(Message, targetOrigin)`: 通过目标窗口的窗口对象引用, 向目标窗口发送消息; targetOrigin接收对象窗口的URL,

### 2.Web Socket通信

> Web Socket是HTML5 提供, 可以在服务器与客户端之间建立一个非HTTP的双向连接, 服务器可以把数据推送到这个socket上;

- `var webSocket = new WebSocket("ws://localhost:8005/socket")`: 创建一个webSocket对象;
- `webSocket.onmessage=function(){...}`: 通过onmessage事件句柄来接收服务器传过来的数据;
- `webSocket.onopen=function(){...}`: 通过onopen事件句柄来监听socket的打开事件;
- `webSocket.onclose=function(){...}`: 通过onclose事件句柄来监听socket的关闭事件;
- `webSocket.close()`: 切断通信连接;

## 9.Web Workers处理线程

> 通过Web Workers可以实现Web平台上的多线程处理功能, 可以创建一个不会影响前台处理的后台线程, 并且在这个后台线程中创建多个子线程;
>
> 后台线程中不能访问页面或窗口对象, 如果使用window对象, document对象, 会引起错误;

- `var worker = new Worker("worker.js")`: 创建后台线程并执行js脚本;
- `worker.onmessage=function(event){...}`: 设置接收后台线程消息的函数(后台线程使用`postMessage()`向创建者发送);
- `worker.postMessage()`: 向后台线程发送消息



## 6.其他

- `<img />`: 嵌入图像
  - `src`: 指定欲嵌入图像的URL, 