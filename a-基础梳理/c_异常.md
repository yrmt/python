
# 异常
## raise
```python
# 语法定义:
raise_stmt ::=  "raise" [expression ["from" expression]]
# from后的参数（必须是另一个异常类或者实例）
# 1. 实例：它将作为__cause__属性附加到引发的异常
# 2. 异常类：该类将被实例化，并且生成的异常实例将作为__cause__属性附加到引发的异常

# 示例
class E(Exception):
    def __init__(self):
        print("*E.__init__*")

    def __str__(self):
        return "*E.__str__*"

raise E from OSError # == raise IndexError from E()

# 打印结果:
OSError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "...", line 9, in <module>
    raise E from OSError  # == raise IndexError from E()
__main__.E: *E.__str__*
E.__init__

```

## 异常基类`BaseException`的`__cause__`属性

导致异常的原因。由于给定的异常，引发了当前的异常。因为X抛出此异常，所以Y必须抛出此异常。

## 异常基类`BaseException`的`__cause__`属性

在尝试处理另一个异常时引发了当前异常，并定义了在引发此异常时正在处理的异常。这是为了您不会丢失其他异常发生的事实（因此在此代码中抛出异常） - 上下文。X 抛出了这个异常，在处理它的同时，Y 也被抛出了。

## 示例
```
try:
    raise Exception("xixi") from OSError
except Exception as e:
    print('e.__cause__: %s' % repr(e.__cause__))
    print('e.__context__: %s' % repr(e.__context__))
    try:
        raise AttributeError()
    except AttributeError as a:
        print('a.__cause__: %s' % repr(a.__cause__))
        print('a.__context__: %s' % repr(a.__context__))
        raise a from e

```


## 打印结果
```
e.__cause__: OSError()
e.__context__: None
a.__cause__: None
a.__context__: Exception('xixi')
OSError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "......", line 2, in <module>
    raise Exception("xixi") from OSError
Exception: xixi

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "......", line 11, in <module>
    raise a from e
  File "......", line 7, in <module>
    raise AttributeError()
AttributeError

```


## 分析
```
  `e`的异常来自于`raise Exception("xixi")`，产生原因是`from OSError` 所以 `e.__cause__`是`OSError()`
  在except中处理`e`时引发了新的`a` 所以`a.__context__` 是 `Exception('xixi')`
  最后我们再抛出异常a并且`from e` 所以整体堆栈看起来就是 OSError -> Exception("xixi") -> AttributeError
```


# 参考资料
1. [Python-raise文档](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement) 
2. [Python-BaseException文档](https://docs.python.org/3/library/exceptions.html#BaseException)
3. [what-is-the-difference-between-cause-and-context](https://stackoverflow.com/questions/11235932/what-is-the-difference-between-cause-and-context)
4. [python-raise-from-usage](https://stackoverflow.com/questions/24752395/python-raise-from-usage)
5. [PEP](https://legacy.python.org/dev/peps/pep-3134/)


