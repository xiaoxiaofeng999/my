$(".typeid").mouseenter(function () {
   var c_id = $(this).attr("c_id");
   var i_id = $(this).attr("i_id");
   console.log(c_id);
   $.ajax({
       type: 'post',
       url: '/yxj/index',
       data: {
           c_id: c_id
       },
       success: function (res) {
           console.log(res);
           $(".dl-sort").remove();
           var a = res.data;
           $(".sort-side").append(
                   "<dl class='dl-sort'></dl>"
               );
           for(var i in a){
               console.log(a[i]);
               $(".dl-sort").append(
                   "<dd><a href='/yxj/prodectlist/"+ c_id +"/2/"+ a[i][1] +"'><span>" + a[i][0] + "</span></a></dd>"
               )
               // console.log("href='/yxj/prodectlist/' i_id '/?secondtype='+ a[i][1] +'")
           }
       }
   })
});
