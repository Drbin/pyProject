$("#addItem").click(function () {
    $(this).before('  <div class="exam_item">\n' +
        '        <div class="exam_tit">\n' +
        '            <input type="text" placeholder="请输入标题"  />\n' +
        '        </div>\n' +
        '        <ul class="exam_class">\n' +
        '            <li>\n' +
        '  <span class="xcheckbox xblue">\n' +
        '                    <label>\n' +
        '                        <input type="checkbox" name="checkbox1[]" /><em></em>\n' +
        '                    </label>\n' +
        '                </span>' +
        '                <input type="text" placeholder="请输入答案"  />\n' +
        '            </li>\n' +
        '            <li>\n' +
        '  <span class="xcheckbox xblue">\n' +
        '                    <label>\n' +
        '                        <input type="checkbox" name="checkbox1[]" /><em></em>\n' +
        '                    </label>\n' +
        '                </span>' +
        '                 <input type="text" placeholder="请输入答案"  />\n' +
        '            </li>\n' +
        '            <li>\n' +
        '  <span class="xcheckbox xblue">\n' +
        '                    <label>\n' +
        '                        <input type="checkbox" name="checkbox1[]" /><em></em>\n' +
        '                    </label>\n' +
        '                </span>' +
        '                 <input type="text" placeholder="请输入答案"  />\n' +
        '            </li>\n' +
        '            <li class="add_item add_item_li">\n' +
        '                +\n' +
        '            </li>\n' +
        '        </ul>\n' +
        '    </div>')
})
$(document).on("click",".add_item_li",function () {
    $(this).before(' <li>\n' +
        '  <span class="xcheckbox xblue">\n' +
        '                    <label>\n' +
        '                        <input type="checkbox" name="checkbox1[]" /><em></em>\n' +
        '                    </label>\n' +
        '                </span>' +
        '                 <input type="text" placeholder="请输入答案"  />\n' +
        '            </li>')
})
$("#submit").click(function () {
    $.ajax({})
})
var model =function () {
    var htmlStr=""
}
class Model {
    htmlStr="<div></div>"

}
var modelBox= new Model();