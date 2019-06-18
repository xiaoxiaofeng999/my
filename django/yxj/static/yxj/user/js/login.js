$(function () {
    $("#sub").click(login());

});

function login() {
    var name = $("#user").val();
    var pwd = $("#password").val();
    // 校验数据
    if (name.length < 3){
        alert("用户名过短");
        return false;
    }
    if (pwd.length < 6){
        alert("密码过短");
        return false;
    }else{
        var enc_pwd = md5(pwd);
        $("#password").val(enc_pwd)
    }
    //     var enc_pwd = md5(pwd);
    // $.ajax({
    //     url:"/yxj/login",
    //     data:{
    //         "name":name,
    //         "pwd":enc_pwd
    //     },
    //     method:"post",
    //     success:function (res) {
    //         if (res.code == 0){
    //             window.open(res.data,target='_self')
    //         }else {
    //             alert(res.msg);
    //         }
    //     },
    //     error:function () {
    //
    //     },
    //     complete:function () {
    //
    //     }
    // });
}
