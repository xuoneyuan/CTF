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
