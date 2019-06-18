$(function () {
    $("#myform").submit(function () {
    //    拿用户名 判断不能为空 并且大于三位
        var name = $("#name").val();
        if (name.length < 3){
            alert("用户名过短");
            //阻止提交
            return false;
        }

        var pwd = $("#password").val();
        var confirm_pwd = $("#passwordRepeat").val();
        if (pwd == confirm_pwd & pwd.length>=6){
        //    做加密
            var enc_pwd = md5(pwd);
            var enc_confirm_pwd = md5(confirm_pwd);
        //    设置回去
            $("#password").val(enc_pwd);
            $("#passwordRepeat").val(enc_confirm_pwd);
        } else {
            alert("密码过短或不一致");
            return false;
        }

    });
});