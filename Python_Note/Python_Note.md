# <mark>Environment</mark>

---



## <mark>安装Python解释器</mark>

`win+r`输入`cmd`

在命令行窗口输入`python`回车

若输出python版本信息就说明安装成功

若无法识别就去微软商店安装,记得点击`add to path`

注：

新建`文本文件`,更改文件后缀为`.py`,然后在编译器或者记事本里写好python代码,就可以进行`多行python`文件运行了

---

## <mark>安装Python开发工具</mark>

`VScode` or `Pycharm`;

这里安装Pycharm:

网址[PyCharm，您需要的唯一 Python IDE](https://www.jetbrains.com/zh-cn/pycharm/);

`创建.py关联`选项，如果只有pycharm一个开发工具那是建议勾选的,如果有多个开发环境那一般不勾选;

`更新上下文菜单`可以右键文件用Pycharm打开,挺好的,建议勾选;

`更新path变量`使Pycharm可以便利地在终端打开,与其他开发工具协作运行,推荐勾选;

---

## <mark>Pycharm使用指南</mark>

### 设置

文件-设置-编辑-常规-自动换行：

勾选`对这些文件进行软换行`,然后把后面默认的那些文件格式都先删掉，

最后输入一个`*.*`，代表对所有文件格式进行软换行



### 项目创建

首先,文件夹名称保持`全英文`,并且`不要带空格`

先在磁盘中`创建Python_projects文件夹`,再在Pycharm中新建项目,选择存储在这个文件夹，选择后不要直接创建项目,要在路径后再加上`\Projects_name`,这样结构会更好

**解释器类型：**

项目venv：虚拟环境运行

基础conda：

自定义环境：



### 项目配置文件

`.venv`为每个项目存放环境，工具信息

`.idea`为每个项目存放配置信息，比如光标最后位置等

一般不需要动这两个文件夹



### 调试

(1)设置断点：

点击代码左侧的行数数字，使该行代码变成红色，表示标记为断点；

后续开发工具会运行到该断电为止，之后可以手动调试

(2)debug调试：

点击“调试”按钮，待程序运行到断点后，可以选择“步过，步入，单步执行，步出”等调试方式

步过就是一步步执行后续代码；



### 快捷键

在代码某一行的任意位置按`Ctrl+/`，该行代码就会被注释("#"),再次按Ctrl+/就会取消注释;

`shift+alt+.`放大代码文字大小,`shift+alt+,`减小代码文字大小;

`Ctrl+d`复制粘贴一次当前行代码到下一行;

`shift+enter`快速创建新的一行，即使光标正处于某行代码中间(这个很有用);

`alt+shift`按住不动,拖动鼠标光标,能进行`列编辑`,同时对多行进行编辑;

`ctrl+y`删除当前行代码;

`alt+p`强制大模型插件智能推荐代码

---

# <mark>Syntax</mark>

---

## 语句结束

**回车**代表语句结束，除非两部分代码写在了同一行，一般不用分号.

## 变量

Python是动态变量，**同一个变量可以存储不同类型的数据**

但还是建议一个变量就存储一个类型的数据

变量必须**赋值后**才能使用

---

# <mark>Streamlit</mark>

> 一个python库 通过它可以依据python语言开发交互式Web界面
> 
> 无需学习所有前端代码知识
> 
> 主要用于数据科学和机器学习



在Pycharm中打开终端PowerShell输入以下安装命令

```powershell
pip install streamlit
```

运行文件:右击文件-在终端中打开-输入`streamlit run xxx.py`

详情学习前往官方网址[Streamlit documentation](https://docs.streamlit.io/)

---

# Problems

## lingma插件

在Pycharm中安装该插件后重启IDE

报错(1):

```powershell

```

报错(2):

```powershell
updateCustomSuggestPrompt error
java.lang.NullPointerException: Cannot invoke "com.alibabacloud.intellij.cosy.db.DataSourceService.isDatasourceExist()" because "dataSourceService" is null
	at com.alibabacloud.intellij.cosy.chat.context.DatabaseContextRefProvider.register(DatabaseContextRefProvider.java:97)
	at com.alibabacloud.intellij.cosy.util.SuggestPromptUtil.updateCustomSuggestPrompt(SuggestPromptUtil.java:192)
	at com.alibabacloud.intellij.cosy.core.lsp.LanguageWebSocketService.refreshCustomCommands(LanguageWebSocketService.java:880)
	at com.alibabacloud.intellij.cosy.core.Cosy.lambda$asyncActionAfterCosyStart$5(Cosy.java:294)
	at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1144)
	at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:642)
	at java.base/java.lang.Thread.run(Thread.java:1583)updateCustomSuggestPrompt error

java.lang.NullPointerException: Cannot invoke "com.alibabacloud.intellij.cosy.db.DataSourceService.isDatasourceExist()" because "dataSourceService" is null
	at com.alibabacloud.intellij.cosy.chat.context.DatabaseContextRefProvider.register(DatabaseContextRefProvider.java:97)
	at com.alibabacloud.intellij.cosy.util.SuggestPromptUtil.updateCustomSuggestPrompt(SuggestPromptUtil.java:192)
	at com.alibabacloud.intellij.cosy.core.lsp.LanguageWebSocketService.refreshCustomCommands(LanguageWebSocketService.java:880)
	at com.alibabacloud.intellij.cosy.core.Cosy.lambda$asyncActionAfterCosyStart$5(Cosy.java:294)
	at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1144)
	at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:642)
	at java.base/java.lang.Thread.run(Thread.java:1583)updateCustomSuggestPrompt error

java.lang.NullPointerException: Cannot invoke "com.alibabacloud.intellij.cosy.db.DataSourceService.isDatasourceExist()" because "dataSourceService" is null
	at com.alibabacloud.intellij.cosy.chat.context.DatabaseContextRefProvider.register(DatabaseContextRefProvider.java:97)
	at com.alibabacloud.intellij.cosy.util.SuggestPromptUtil.updateCustomSuggestPrompt(SuggestPromptUtil.java:192)
	at com.alibabacloud.intellij.cosy.core.lsp.LanguageWebSocketService.refreshCustomCommands(LanguageWebSocketService.java:880)
	at com.alibabacloud.intellij.cosy.core.Cosy.lambda$asyncActionAfterCosyStart$5(Cosy.java:294)
	at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1144)
	at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:642)
	at java.base/java.lang.Thread.run(Thread.java:1583)
```
