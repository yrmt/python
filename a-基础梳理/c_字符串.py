"""
@author: yrmt
@contact: butanoler@gmail.com
@file: c_字符串.py
@time: 2019/8/15
"""
# format ^居中 <左对齐 >右对齐
# ljust 左对齐 rjust 右对齐
# 数字格式化 {:.2f} 保留两位小数


# 练习 输出
# 01.base      3页
# 02.net       2页
# 03.flask     2页
names = ['base', 'net', 'flask']
pages = [3, 2, 2, 1]
max_len = len(max(names, key=len))
one_line_format = lambda index, key, value: "# {:02d}.{}{}条".format(index + 1, str(key).ljust(max_len + 4), value)
print_str = '\n'.join((
    one_line_format(index, key, value) for index, (key, value) in enumerate(dict(zip(names, pages)).items())
))

print(print_str)
