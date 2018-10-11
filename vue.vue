<div id="example">
    <div>
        <span>{{message}}</span>
        <span :class="">{{newMessave}}</span>
    </div>
</div>


<script>
    var vm = new Vue({
        el: '#example',
        // 选项/数据 https://cn.vuejs.org/v2/api/#%E9%80%89%E9%A1%B9-%E6%95%B0%E6%8D%AE
        // vue实例数据对象
        data: {
            message: 'hello'
        },
        // 计算属性, 属性值由计算得到
        computed: {
            newMessave:()=>{return this.message.toUpperCase()},
            set_get_message:{
                get: ()=>{},
                // 当主动对计算属性赋值时set方法会调用
                set: ()=>{}
            }
        },
        // 监听, 键是监听的表达式, 值是对应的回调函数
        watch: {
            message: ()=>{console.log(this.message)}
        }
    })
</script>


<style>
    .error{
        color: red;
    }

</style>