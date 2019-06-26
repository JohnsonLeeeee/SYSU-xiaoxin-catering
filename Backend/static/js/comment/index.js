;
var comment_index_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        var that = this;

        $(".addblack").click( function(){
            that.ops( "addblack",$(this).attr("data") );
        } );

    },
    ops:function( act,id ){
        var callback = {
            'ok':function(){
                $.ajax({
                    url:common_ops.buildUrl( "/comment/ops" ),
                    type:'POST',
                    data:{
                        act:act,
                        id:id
                    },
                    dataType:'json',
                    success:function( res ){
                        var callback = null;
                        if( res.code == 200 ){
                            callback = function(){
                                window.location.href = window.location.href;
                            }
                        }
                        common_ops.alert( res.msg,callback );
                    }
                });
            },
            'cancel':null
        };
        common_ops.confirm( "确定加入黑名单？", callback );
    }

};

$(document).ready( function(){
    comment_index_ops.init();
} );