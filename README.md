# 中国大学计算机门类《C 语言程序设计》课后习题库（合规版）

本仓库用于建设 **C 语言课程习题库框架**，面向中国大学计算机相关专业课程使用。

## 合规说明

- 本仓库**不直接收录受版权保护教材的全文和原版课后题原文**。
- 本仓库提供：
  1. 可公开获取或可合法购买的教材清单；
  2. 按知识点组织的练习题库（原创/改写题）；
  3. 题库扩展规范与章节化模板，便于持续补充。

## 一、教材参考（公开目录信息）

> 建议通过出版社官网、学校图书馆、MOOC 平台或正规电商获取正版教材与配套资源。

1. 《C程序设计（第五版）》谭浩强，清华大学出版社  
2. 《C语言程序设计现代方法（第2版）》K.N. King（中译本）  
3. 《C Primer Plus（第6版）》Stephen Prata（中译本）  
4. 《The C Programming Language（第2版）》Kernighan & Ritchie（中译本）  
5. 《程序设计基础（C语言）》高等教育出版社相关版本（各校常用）  
6. 《C语言程序设计教程》机械工业出版社相关版本（各校常用）  
7. 《C程序设计试题汇编（第三版）》谭浩强 主编，清华大学出版社（你提供的封面）

## 二、章节化题库索引

- [Chapter 01 程序设计基础与开发环境](./chapters/ch01.md)
- [Chapter 02 基本数据类型、常量与变量](./chapters/ch02.md)
- [Chapter 03 运算符与表达式](./chapters/ch03.md)
- [Chapter 04 顺序、分支结构](./chapters/ch04.md)
- [Chapter 05 循环结构](./chapters/ch05.md)
- [Chapter 06 数组](./chapters/ch06.md)
- [Chapter 07 函数](./chapters/ch07.md)
- [Chapter 08 指针](./chapters/ch08.md)
- [Chapter 09 字符串](./chapters/ch09.md)
- [Chapter 10 结构体与共用体](./chapters/ch10.md)
- [Chapter 11 文件操作](./chapters/ch11.md)
- [Chapter 12 综合实践](./chapters/ch12.md)

> 每章包含 5 题，并已补齐：题目、输入要求、输出要求、样例输入、样例输出、参考答案模板。

## 三、知识库与自动生成目录

```text
Laidecai/-C-/
├── .github/
│   └── copilot-instructions.md
├── knowledge-base/
│   ├── textbook_chapters/
│   └── question_bank/
├── exercises/
│   └── chapter03/
└── scripts/
```

- `knowledge-base/textbook_chapters/`：教材章节知识点改写摘要。
- `knowledge-base/question_bank/`：结构化题库源数据（章节 JSON/MD）。
- `scripts/`：从知识库自动生成习题索引与代码模板的脚本。
- `exercises/chapter03/`：第三章自动生成产物（阅读题答案索引 + 编程题 C 源码）。

## 四、题库扩展规范（增强版）

### 1) 目录与命名规范

- 章节文件：`/chapters/chXX.md`
- 题号格式：`CHxx-Qyyy`
- 推荐按难度标记：`基础 / 进阶 / 挑战`

### 2) 每题最小字段（必须）

1. 题号
2. 题目描述
3. 输入要求
4. 输出要求
5. 样例输入
6. 样例输出
7. 参考答案模板（可运行骨架或理论答题模板）
8. 知识点
9. 难度

### 3) 质量要求

- 样例输入输出要自洽，可直接用于课堂讲解或实验指导。
- 代码模板需包含基础错误处理（如非法输入、除零、文件打开失败等）。
- 理论题必须给出答题要点模板，避免只留标题。
- 题目应避免直接复刻教材原题原文，优先采用原创/改写表述。

### 4) 扩展建议

- 每章补充“基础/进阶/挑战”分层题单。
- 为代码题增加边界样例（空输入、极值、异常输入）。
- 后续可加入自动评测字段：`time_limit`、`memory_limit`、`checker`。

## 五、Chapter03 自动拉取与生成

从以下源文件自动生成第三章作业目录：

- `knowledge-base/question_bank/ch03_exercises.md`

执行命令：

```bash
python scripts/generate_chapter03_exercises.py
```
