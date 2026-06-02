# 第三章习题（结构化题库）

> 教学用途：`阅读程序写结果` + `编程题`。
> 合规说明：以下题干为根据教材知识点整理后的改写版训练题，不是教材原文逐字摘录。

<!-- AUTO-DATA-BEGIN -->
```json
{
  "chapter": "03",
  "chapter_title": "运算符与表达式",
  "book_refs": [
    "《C程序设计（第五版）》",
    "《C程序设计试题汇编（第三版）》"
  ],
  "reading_questions": [
    {
      "id": "R03-01",
      "type": "阅读程序写结果",
      "prompt": "给定 i=2, j=3，执行 k = i++ + ++j; 输出 i, j, k。",
      "answer": "i=3, j=4, k=6",
      "analysis": "i++ 先取值 2 后自增为 3；++j 先自增为 4 再参与运算。"
    },
    {
      "id": "R03-02",
      "type": "阅读程序写结果",
      "prompt": "给定 int a=5; double b=2; printf(\"%.1f\\n\", a/b); 输出是什么？",
      "answer": "2.5",
      "analysis": "a 在表达式中提升为 double，执行浮点除法。"
    },
    {
      "id": "R03-03",
      "type": "阅读程序写结果",
      "prompt": "表达式 (x!=0) && (10/x>1) 在 x=0 时右侧是否执行？",
      "answer": "不执行",
      "analysis": "&& 存在短路；左侧为假时右侧不求值。"
    }
  ],
  "programming_questions": [
    {
      "id": "P03-01",
      "filename": "p03_01_max_ternary.c",
      "template_file": "knowledge-base/question_bank/templates/chapter03/p03_01_max_ternary.c",
      "title": "使用条件运算符求两个整数最大值",
      "knowledge_point": "条件运算符 ?:、整型输入输出",
      "prompt": "输入两个整数 a、b，输出较大值。",
      "input_spec": "一行两个整数",
      "output_spec": "输出一个整数，为 max(a,b)",
      "sample_input": "3 9",
      "sample_output": "9"
    },
    {
      "id": "P03-02",
      "filename": "p03_02_mod_negative.c",
      "template_file": "knowledge-base/question_bank/templates/chapter03/p03_02_mod_negative.c",
      "title": "验证负数取模结果",
      "knowledge_point": "取模运算 %、输入校验（除数不能为 0）",
      "prompt": "输入两个整数 a、b（b != 0），输出 a % b 的结果。",
      "input_spec": "一行两个整数，第二个数非 0",
      "output_spec": "输出一个整数",
      "sample_input": "-7 3",
      "sample_output": "-1"
    },
    {
      "id": "P03-03",
      "filename": "p03_03_type_cast_average.c",
      "template_file": "knowledge-base/question_bank/templates/chapter03/p03_03_type_cast_average.c",
      "title": "计算两数平均值（保留两位小数）",
      "knowledge_point": "类型转换、浮点输出格式",
      "prompt": "输入两个整数 a、b，输出其平均值，保留两位小数。",
      "input_spec": "一行两个整数",
      "output_spec": "输出一个浮点数，格式 %.2f",
      "sample_input": "5 8",
      "sample_output": "6.50"
    }
  ]
}
```
<!-- AUTO-DATA-END -->
