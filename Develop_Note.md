# Study Note

1. [pypinyin doc](https://pypinyin.readthedocs.io/zh_CN/master/usage.html#example)

2. `json.dump` 导出文件的中文字符变为 unicode 字符问题

> If ensure_ascii is true (the default), the output is guaranteed to have all incoming non-ASCII characters escaped. If ensure_ascii is false, these characters will be output as-is.

解决 :  
`json.dumps(d, ensure_ascii=False)`
