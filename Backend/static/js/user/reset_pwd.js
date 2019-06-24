;
var mod_pwd_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        $("#save").click(function(){
            var btn_target = $(this);
            if( btn_target.hasClass("disabled") ){
                common_ops.alert("正在处理!!请不要重复提交~~");
                return;
            }

            var old_password = $("#old_password").val();
            var new_password = $("#new_password").val();
            var repeat_password = $("#repeat_password").val();


            if( !old_password ){
                common_ops.alert( "请输入原密码~~" );
                return false;
            }

            if( !new_password || new_password.length < 6 ){
                common_ops.alert( "请输入不少于6位的新密码~~" );
                return false;
            }
            console.log(new_password)
            console.log(old_password)
            console.log(typeof(old_password) )
             if( repeat_password != new_password ){
                common_ops.alert( "两次输入的新密码要一致~~" );
                return false;
            }

            btn_target.addClass("disabled");

            var data = {
                old_password: old_password,
                new_password: new_password,
                repeat_password:repeat_password
            };

            $.ajax({
                url:common_ops.buildUrl( "/user/reset-pwd" ),
                type:'POST',
                data:data,
                dataType:'json',
                success:function( res ){
                    btn_target.removeClass("disabled");
                    var callback = null;
                    if( res.code == 200 ){
                        callback = function(){
                            window.location.href = window.location.href;
                        }
                    }
                    common_ops.alert( res.msg,callback );
                }
            });


        });
    }
};

$(document).ready( function(){
    mod_pwd_ops.init();
} );