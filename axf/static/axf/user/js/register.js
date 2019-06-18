$(function () {
    $("#myform").submit(function () {
        // 拿用户名 判断不能为空 并且大于三位
        var name = $("#uid").val();
        if (name.length < 3){
            alert("用户名过短")
            //阻止提交
        }
        var pwd = $("#u_pwd").val();
        var confirm_pwd = $("#u_confirm_pwd").val();
        if (pwd == confirm_pwd & pwd.length >= 6){
            //做加密
            var enc_pwd = md5(pwd);
            var enc_confirm_pwd = md5(confirm_pwd);
            //加密完后已经不在form中了 ，要加入回去
            $("#u_pwd").val(enc_pwd);
            $("#u_confirm_pwd").val(enc_confirm_pwd);

        }else {
            alert("密码过短或不一致");
            return false;
        }
    });
    $("#uid").change(function () {
        var uname = $("#uid").val();
        $.ajax({
           url:"/myaxf/check_uname",
           data:{
               //uname是对象里面的属性了
               uname:uname
           },
           method:"get",
           success:function (res) {
               //提示用户 判断请求是否是成功的请求
               if (res.code ==1){
                   $("#uname_msg").html(res.msg)
               }else { // 错误提示
                   alert(res.msg);
               }
           }
        });
    })

})