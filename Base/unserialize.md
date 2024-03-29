## 反序列化
把字节序列恢复为对象的过程，即把可以存储或传输的数据转换为对象的过程。例如将二进制数据流或文件加载到内存中还原为对象。

使用unserialize()函数

$u=unserialize("O:1:"S":1:{s:4:"test";s:2:"sd";}");

echo $u->test; //得到的结果为sd

## 反序列化安全

序列化和反序列化本身没有问题,但是如果反序列化的内容是用户可以控制的,且后台不正当的使用了PHP中的魔法函数,就会导致安全问题

有哪些php常见的魔法函数:

__construct() 当一个对象创建时被调用\
__destruct() 当一个对象销毁前被调用\
__sleep() 在对象被序列化前被调用\
__wakeup 将在反序列化之后立即被调用\
__toString 当一个对象被当做字符串使用时被调用\
__get(),__set() 当调用或设置一个类及其父类方法中未定义的属性时\
__invoke() 调用函数的方式调用一个对象时的回应方法\
__call 和 __callStatic前者是调用类不存在的方法时执行，而后者是调用类不存在的静态方式方法时执行


## JAVA反序列化
序列化和反序列化的实现\
1.  JDK类库提供的序列化API\
java.io.ObjectOutputStream：表示对象输出流\
它的writeObject(Object obj)方法可以对参数指定的obj对象进行序列化，把得到的字节序列写到一个目标输出流中。\
java.io.ObjectInputStream：表示对象输入流\
它的readObject()方法从源输入流中读取字节序列，再把它们反序列化成为一个对象，并将其返回。\
2.  实现序列化的要求\
只有实现了Serializable或Externalizable接口的类的对象才能被序列化，否则抛出异常。\
3. 实现Java对象序列化与反序列化的方法\
假定一个Student类，它的对象需要序列化，可以有如下三种方法：

方法一：若Student类仅仅实现了Serializable接口，则可以按照以下方式进行序列化和反序列化。\
ObjectOutputStream采用默认的序列化方式，对Student对象的非transient的实例变量进行序列化。\
ObjcetInputStream采用默认的反序列化方式，对对Student对象的非transient的实例变量进行反序列化。

方法二：若Student类仅仅实现了Serializable接口，并且还定义了readObject(ObjectInputStream in)和writeObject(ObjectOutputSteam out)，则采用以下方式进行序列化与反序列化。\
ObjectOutputStream调用Student对象的writeObject(ObjectOutputStream out)的方法进行序列化。\
ObjectInputStream会调用Student对象的readObject(ObjectInputStream in)的方法进行反序列化。

方法三：若Student类实现了Externalnalizable接口，且Student类必须实现readExternal(ObjectInput in)和writeExternal(ObjectOutput out)方法，则按照以下方式进行序列化与反序列化。\
ObjectOutputStream调用Student对象的writeExternal(ObjectOutput out))的方法进行序列化。\
ObjectInputStream会调用Student对象的readExternal(ObjectInput in)的方法进行反序列化。
