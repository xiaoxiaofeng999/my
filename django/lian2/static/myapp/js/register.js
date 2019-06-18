$(function () {

    $("#myform").submit(function () {
        alert("hehe");
        //    拿用户名 判断不能为空 并且大于三位
        var name = $("#uid").val();
        if (name.length < 1) {
            alert("请输入。。。");
            //阻止提交
            return false;
        }
        if (name.length < 3) {
            alert("用户名过短，请重新输入_-_")
        }
        var pwd = $("#u_pwd").val();
        var confirm_pwd = $("#u_confirm_pwd").val();
        if (pwd == confirm_pwd & pwd.length >= 6) {
            //    做加密
            var enc_pwd = md5(pwd);
            var enc_confirm_pwd = md5(confirm_pwd);
            //    设置回去
            $("#u_pwd").val(enc_pwd);
            $("#u_confirm_pwd").val(enc_confirm_pwd);
        } else {
            alert("密码过短或不一致");
            return false;
        }

    });

    $("#uid").change(function () {
        alert("进入建议");
        var uname = $("#uid").val();
        $.ajax({
            url: "/myapp/check_uname",
            data: {
                uname: uname
            },
            method: "get",
            success: function (res) {
                //    提示用户
                if (res.code == 1) {
                    $("#uname_msg").html(res.msg);
                } else {
                    //错误提示
                    alert(res.msg);
                }
            }
        });


    });


      $("#u_pwd").change(function () {
            alert("进入建议");
            var u_pwd = $("#u_pwd").val();
            // console.log(pwd);
            $.ajax({
                url: "/myapp/check_upwd",
                data: {
                    u_pwd: u_pwd
                },
                method: "get",
                success: function (res) {
                    //    成功
                    if (res.code == 1) {
                        $("#pwd_msg").html(res.msg);

                    }else if (res.code == 2) {
                        //提示用户密码必须包含数字、大小写英文字母
                        $("#pwd_msg").html(res.msg);
                    }else {
                         //错误提示
                        alert(res.msg);
                    }
                }
            });

        });
});