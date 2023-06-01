~~~
package com.testjava.jack.pingan1;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

/* loaded from: classes.dex */
public class MainActivity extends AppCompatActivity {
    /* JADX INFO: Access modifiers changed from: protected */
    @Override // android.support.v7.app.AppCompatActivity, android.support.v4.app.FragmentActivity, android.support.v4.app.SupportActivity, android.app.Activity
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button btn = (Button) findViewById(R.id.button);
        btn.setOnClickListener(new View.OnClickListener() { // from class: com.testjava.jack.pingan1.MainActivity.1
            @Override // android.view.View.OnClickListener
            public void onClick(View view) {
                EditText edit1 = (EditText) MainActivity.this.findViewById(R.id.editText);
                String strIn = edit1.getText().toString();
                Base64New nb = new Base64New();
                String enStr = nb.Base64Encode(strIn.getBytes());
                if (enStr.equals("5rFf7E2K6rqN7Hpiyush7E6S5fJg6rsi5NBf6NGT5rs=")) {
                    Toast.makeText(MainActivity.this, "验证通过!", 1).show();
                } else {
                    Toast.makeText(MainActivity.this, "验证失败!", 1).show();
                }
            }
        });
    }
}
~~~

- 这是一个用于Android应用程序的Java代码。
- 该代码定义了一个类MainActivity，它扩展了AppCompatActivity类，这是Android支持库的一部分，用于向后兼容。onCreate方法是一个重写的方法，当活动被创建时被调用。
- setContentView方法使用activity_main布局文件设置活动的布局。
- 然后，代码使用findViewById方法找到一个名为btn的按钮，并在其上设置一个点击监听器。当按钮被点击时，将调用onClick方法。
- 在onClick方法内部，代码找到一个名为EditText的视图并获取其文本。然后，它创建Base64New类的一个实例，并使用Base64Encode方法对文本进行编码。
- 如果编码后的字符串与特定值匹配，则应用程序将显示一个成功消息。否则，它会显示一个失败消息。

Base64New:
package com.testjava.jack.pingan1;
~~~
/* loaded from: classes.dex */
public class Base64New {
    private static final int RANGE = 255;
    private static final char[] Base64ByteToStr = {'v', 'w', 'x', 'r', 's', 't', 'u', 'o', 'p', 'q', '3', '4', '5', '6', '7', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'y', 'z', '0', '1', '2', 'P', 'Q', 'R', 'S', 'T', 'K', 'L', 'M', 'N', 'O', 'Z', 'a', 'b', 'c', 'd', 'U', 'V', 'W', 'X', 'Y', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', '8', '9', '+', '/'};
    private static byte[] StrToBase64Byte = new byte[128];

    public String Base64Encode(byte[] bytes) {
        StringBuilder res = new StringBuilder();
        for (int i = 0; i <= bytes.length - 1; i += 3) {
            byte[] enBytes = new byte[4];
            byte tmp = 0;
            for (int k = 0; k <= 2; k++) {
                if (i + k <= bytes.length - 1) {
                    enBytes[k] = (byte) (((bytes[i + k] & 255) >>> ((k * 2) + 2)) | tmp);
                    tmp = (byte) ((((bytes[i + k] & 255) << (((2 - k) * 2) + 2)) & 255) >>> 2);
                } else {
                    enBytes[k] = tmp;
                    tmp = 64;
                }
            }
            enBytes[3] = tmp;
            for (int k2 = 0; k2 <= 3; k2++) {
                if (enBytes[k2] <= 63) {
                    res.append(Base64ByteToStr[enBytes[k2]]);
                } else {
                    res.append('=');
                }
            }
        }
        return res.toString();
    }
}
~~~
更改了base64解密方式

payload：
~~~
import base64
now = ['v', 'w', 'x', 'r', 's', 't', 'u', 'o', 'p', 'q', '3', '4', '5', '6', '7', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'y', 'z', '0', '1', '2', 'P', 'Q', 'R', 'S', 'T', 'K', 'L', 'M', 'N', 'O', 'Z', 'a', 'b', 'c', 'd', 'U', 'V', 'W', 'X', 'Y', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', '8', '9', '+', '/']
now = "".join(now)
original = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
str1 = '5rFf7E2K6rqN7Hpiyush7E6S5fJg6rsi5NBf6NGT5rs='
print("flag{"+base64.b64decode(str1.translate(str.maketrans(now, original)).encode('utf-8')).decode('utf-8')+"}")
~~~

- 该代码使用Python中的base64库进行编码和解码操作。
- 首先，代码定义了一个列表now，其中包含一些字符。然后，将这些字符拼接成一个字符串now。接下来，定义一个字符串original，它包含所有Base64编码字符。
- 然后，定义一个字符串str1，它是一个Base64编码后的字符串。
- 代码使用str.maketrans()方法将now和original两个字符串映射起来，然后使用translate()方法将str1中的所有now字符替换为original中对应的字符。
- 接着，代码使用base64.b64decode()方法对经过映射的字符串进行解码。最后，将解码后的字符串与固定字符串flag{}拼接起来输出，从而构成一个Flag。

"".join(now)是将列表now中的所有元素按照空字符串""进行连接，并返回一个新的字符串。
具体来说，它将列表now中的每个元素按照顺序连接起来，不使用任何分隔符，生成一个字符串。例如，如果now列表包含["a", "b", "c"]，则"".join(now)将返回字符串"abc"。
在这个代码中，将列表now中的所有元素连接成一个字符串是为了方便后续的字符串映射操作。

translate() 方法是Python中字符串对象的一个方法，用于将字符串中的某些字符替换为其他字符。它需要一个字符串映射表作为参数，可以使用 str.maketrans() 方法来创建这个映射表。

str.maketrans() 方法用于创建两个字符之间的映射表。它需要两个参数，这两个参数都应该是字符串，其中第一个参数是需要被替换的字符，第二个参数是替换后的字符，它们应该一一对应。例如：

table = str.maketrans("abc", "123")

上面的代码将创建一个字符串映射表，将字符串中的字符 a 替换为 1，将字符 b 替换为 2，将字符 c 替换为 3。

接着，将这个映射表作为参数传递给 translate() 方法，即可将字符串中的指定字符替换为映射表中的对应字符。例如：

text = "apple"
new_text = text.translate(table)
print(new_text)  # 输出：'1pple'
在这个代码中，translate() 方法将 text 中的 a 替换为 1，将 b 替换为 2，将 c 替换为 3。因此，最终得到的新字符串为 '1pple'。

在本题中，translate() 方法和 str.maketrans() 方法的组合用于将 Base64 编码中的一组字符替换为另一组字符，从而生成一个新的 Base64 编码字符串。
