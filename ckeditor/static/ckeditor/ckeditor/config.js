/**
 * @license Copyright (c) 2003-2016, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.md or http://ckeditor.com/license
 */

CKEDITOR.editorConfig = function (config) {
    // Define changes to default configuration here. For example:
    // config.language = 'fr';
    // config.uiColor = '#AADC6E';

    config.language = 'zh-cn';
    //config.extraPlugins = 'clipboard,codesnippet,dialog,lineutils,widget';
    config.font_names = '宋体/宋体;黑体/黑体;仿宋/仿宋_GB2312;楷体/楷体_GB2312;隶书/隶书;幼圆/幼圆;微软雅黑/微软雅黑;' + config.font_names;
    config.codeSnippet_theme = 'Monokai'; 'xcode', 'Monokai'; 'Magula', 'Idea', 'Foundation', 'Docco', 'Default','Vs','Monokai','pojoaque';

    //ckeditor默认的换行是：enter->加<p></p>，shift+enter->加<br />, 我们反过来设置
    config.enterMode = CKEDITOR.ENTER_BR;
    config.shiftEnterMode = CKEDITOR.ENTER_P;
};
