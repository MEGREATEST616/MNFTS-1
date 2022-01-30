$(function(){
    // 点击菜单按钮切换
    $(".menu").click(function(){
        $(this).toggleClass("active")
        $(".nav").slideToggle()
    })


})