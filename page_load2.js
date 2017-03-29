var page = require('webpage').create();
page.settings.userAgent = 'EasyPass';
var url = 'http://bi.rayjoy.com/bi_xhc/boss/user_view/view';
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


