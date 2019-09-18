$("#addItem").click(function () {
    $(this).before('  <div class="exam_item">\n' +
        '        <div class="exam_tit">\n' +
        '            <input type="text" placeholder="请输入标题"  />\n' +
        '        </div>\n' +
        '        <ul class="exam_class">\n' +
        '            <li>\n' +
        '                <input type="text" placeholder="请输入答案"  />\n' +
        '            </li>\n' +
        '            <li>\n' +
        '                 <input type="text" placeholder="请输入答案"  />\n' +
        '            </li>\n' +
        '            <li>\n' +
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
        '                 <input type="text" placeholder="请输入答案"  />\n' +
        '            </li>')
})