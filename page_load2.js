var page = require('webpage').create();
page.settings.userAgent = 'EasyPass';
var url = 'http://www.baidu.com';
t = Date.now()
page.open(url, function(status) {
    console.log(status)
    if(status=='success'){
     sub= Date.now() - t;
     console.log(sub)
     page.render('example3.png');
    }else{
    console.log(status)
    }
    phantom.exit();
});


