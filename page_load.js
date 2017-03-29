var page = require('webpage').create();
var url = 'http://bi.rayjoy.com/yama-frontend';
page.open(url, function(status) {
    var title = page.evaluate(function() {
        return document.title;
    });
    console.log('Page title is ' + title);
    phantom.exit();
});