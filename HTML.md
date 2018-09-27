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
- 全局属性: 所有元素都可配置
  - `class`: 类
  - `contenteditable`: 使用户可以修改其上内容; 
  - `draggable`: 可以拖放;
  - `hidden`: 隐藏;
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

- `<section></section>`: h5, 表示文档中的一节;

- `<header></header>`: 表示一节的首部, 可包含各种适合出现在首部的东西, 包括刊头或徽标;

- `<footer></footer>`: 表示一节尾部.

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


### 文字相关元素

- `<b></b>`: 标记一段文字, 但并不代表特别强调或重要性; 
- `<i></i>`: 表示这段文字与周围内容有本质区别;
- `<s></s>`: 表示一段文字不准确或校正;
- `<sub></sub>, <sup></sup>`: 下标或上标;
- `<wbr>`: 建议换行;

## 4.表单标签

- `<form></form>`: 表单
  - `action="/test/tset"`: 应该将数据发送到的地方;
  - `method="post"`: 表单提交方式;
  - `name`: 可用于css选择, 不发送到浏览器;
- `<input></input>`: 
  - `autofocus`: 自动聚焦, 表单显示的时候就聚焦于某个input元素; 
  - `disabled`: 禁用;
  - `type`: 类型, 
- `button`: 按钮
  - `type`: submit, 提交表单(默认); reset, 重置表单; button, 仅为一个按钮, 
  - `form`: h5, 通过form与任意表单挂钩;

- `<label></label>`: 

## 5.嵌入内容

- `<img />`: 嵌入图像
  - `src`: 指定欲嵌入图像的URL, 