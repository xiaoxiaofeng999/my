$(function () {
    $("#submit").click(login);

});

function login() {
    // 拿到用户
    var name = $("#uid").val();
    var pwd = $("#u_pwd").val();
    if (name.length<3){
        alert("用户名过短");
        return false
    }
    if (pwd.length<6){
        alert("密码过短");
        return false
    }
    //3.给密码做md5
    var enc_pwd = md5(pwd);
    //4.发送Ajax请求
    $.ajax({
        url:"/myaxf/login",
        data:{
            "name":name,
            "pwd":enc_pwd
        },
        method:"post",
        success:function (res) {
            //如果成功 就跳转到mine.html
            if (res.code ==1){
                window.open(res.data,target="_self")
            }else {
                // 如果失败 提示用户
                alert(res.msg)
            }
        },
        error:function () {

        },
        complete:function () {

        }
    });
}