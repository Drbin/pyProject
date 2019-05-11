     var fileType=["png","jpg","jpeg","gif"]; //根据需要添加文件类型
/**
 * 调用方法picUpload()
 * @param dom 图片上传的盒子标签
 * @param callback  回调函数 可将图片上传方法写入
 *@param showArr 回显图片地址
 *
 * */
     function picUpload(dom,callback,showArr) {
         var str="";
         if (showArr!==undefined){
             for (var i=0;i<showArr.length;i++){
                str+="<li><input type='file' title='' onchange='fileLoad(this)' ><img src='"+showArr[i]+"' ><div class='del' onclick='del($(this))'><span>×</span></div></li>"
            }
         }

        var initStr="<ul class='init_str'>" +
            str+
            "<li><input type='file' title='' onchange='fileLoad(this)' ></li>" +
            "</ul>" +
            "<button class='init_upload' >上传</button>";
        $(dom).append(initStr);
        $(dom+" .init_upload").click(function () {

            uploads(dom,callback)
        })
    }

     function suffix(str){
        var suffix=str.substring(str.lastIndexOf(".")+1,str.length);
        return suffix.toLowerCase();
     }
      function getObjectURL(file) {
          var url = null ;
          if (file!==undefined){
             if (window.createObjectURL!=undefined) { // basic
                 url = window.createObjectURL(file) ;
             } else if (window.URL!=undefined) { // mozilla(firefox)
                 url = window.URL.createObjectURL(file) ;
             } else if (window.webkitURL!=undefined) { // webkit or chrome
                url = window.webkitURL.createObjectURL(file) ;
             }
          }
          return url ;
      }
     function del(dom) {
          layer.confirm('是否删除图片？', {
              btn: ['是','否'] //按钮
            },
            function(index){
              dom.parent().remove();
              layer.close(index)
            }
          );
     }
     function uploads(dom,callback) {
         var file=[];
         $.each($(dom+" input[type=file]"),function () {
             if(this.files[0]!==undefined)
                file.push(this.files[0])
         })
         callback(file)
     }
     function fileLoad(dom) {
         var flag=0;
          var url=getObjectURL(dom.files[0]);
          var suf= suffix(dom.files[0].name);
          for (var i=0;i<fileType.length;i++){
              if(fileType[i]==suf){
                flag++;
              }
          }
          if (flag===0){
              $(dom).val("")
              layer.open({
                 content:"请选择正确格式文件"
              });
              return false;
          }else{
             if($(dom).find("img").length>0){
                $(dom).find("img").attr("src",url)
             }else{
                  $(dom).parent().css("background","none").append("<img src='"+url+"' ><div class='del' onclick='del($(this))'><span>×</span></div>").after("<li><input type='file'  title='' onchange='fileLoad(this)' ></li>")
             }
          }
    }
