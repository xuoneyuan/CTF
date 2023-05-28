### Apache Shiro是一个全面的、蕴含丰富功能的安全框架

##### Shiro有三大核心组件，即Subject、SecurityManager 和 Realm
- Subject: 为认证主体。应用代码直接交互的对象是Subject,Subject代表了当前的用户。包含Principals和Credentials两个信息。
- SecurityManager:为安全管理员。是Shiro架构的核心。与Subject的所有交互都会委托给SecurityManager, Subject相当于是一个门面，而SecurityManager才是真正的执行者。它负责与Shiro 的其他组件进行交互。
- Realm：是一个域。充当了Shiro与应用安全数据间的“桥梁”。Shiro从Realm中获取安全数据（如用户、角色、权限），就是说SecurityManager要验证用户身份，那么它需要从Realm中获取相应的用户进行比较，来确定用户的身份是否合法；也需要从Realm得到用户相应的角色、权限，进行验证用户的操作是否能过进行，可以把Realm看成DataSource，即安全数据源。

##### Authentication（认证）, Authorization（授权）, Session Management（会话管理）, Cryptography（加密）被 Shiro 框架的开发团队称之为应用安全的四大基石。那么就让我们来看看它们吧：

1. Authentication（认证）：用户身份识别，通常被称为用户“登录”
2. Authorization（授权）：访问控制。比如某个用户是否具有某个操作的使用权限。
3. Session Management（会话管理）：特定于用户的会话管理,甚至在非web 或 EJB 应用程序。
4. Cryptography（加密）：在对数据源使用加密算法加密的同时，保证易于使用。

还有其他的功能来支持和加强这些不同应用环境下安全领域的关注点。特别是对以下的功能支持：

- Web支持：Shiro的Web支持API有助于保护Web应用程序。
- 缓存：缓存是Apache Shiro API中的第一级，以确保安全操作保持快速和高效。
- 并发性：Apache Shiro支持具有并发功能的多线程应用程序。
- 测试：存在测试支持，可帮助您编写单元测试和集成测试，并确保代码按预期得到保障。
- “运行方式”：允许用户承担另一个用户的身份(如果允许)的功能，有时在管理方案中很有用。
- “记住我”：记住用户在会话中的身份，所以用户只需要强制登录即可。


### 相关CVE
| 漏洞编号           | Shiro版本                  | 配置                    | 漏洞形式                |
|-------------------|----------------------------|-------------------------|-------------------------|
| CVE-2010-3863     | shiro < 1.1.0 和JSecurity 0.9.x | /** = anon          | /./remoting.jsp         |
| CVE-2014-0074/SHIRO-460 | shiro 1.x < 1.2.3     | -                       | ldap、空密码、空用户名、匿名 |
| CVE-2016-4437/SHIRO-550 | shiro 1.x < 1.2.5     | -                       | RememberMe、硬编码          |
| CVE-2016-6802     | shiro < 1.3.2              | Context Path绕过           | /x/../context/xxx.jsp  |
| CVE-2019-12422/SHIRO-721 | shiro < 1.4.2        | -                       | RememberMe、Padding Oracle Attack、CBC |
| CVE-2020-1957/SHIRO-682 | shiro < 1.5.2        | /** = anon             | /toJsonPOJO/、Spring Boot < 2.3.0.RELEASE -> /xx/..;/toJsonPOJO |
| CVE-2020-11989/SHIRO-782 | shiro < 1.5.3        | (等于1.5.2）/toJsonList/* = authc；(小于1.5.3）/alter/* = authc && /** = anon | (等于1.5.2）/的两次编码 -> %25%32%66 /toJsonList/a%25%32%66a ->/toJsonList/a%2fa；（小于1.5.3）/;/shirodemo/alter/test -> /shirodemo/alter/test (Shiro < 1.5.2版本的话，根路径是什么没有关系) |
| CVE-2020-13933     | shiro < 1.6.0              | /hello/* = authc          | /hello/%3ba             |
| CVE-2020-17510    | shiro < 1.7.0              | /hello/* = authc          | /hello/%2e              |
| CVE-2020-17523    | shiro < 1.7.1              | /hello/* = authc          | /hello/%20              |
| CVE-2021-41303    | shiro < 1.8.0              | /admin/* = authc && /admin/page = anon | /admin/page/         |
| CVE-2022-32532    | shiro < 1.9.1              | RegExPatternMatcher && /alter/.* |                        |
