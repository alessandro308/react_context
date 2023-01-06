
# react_context

An API to pass data down in the sub-function inspired by React Context

```
pip install react-context
```

Inspired by [this reddit](https://discuss.python.org/t/react-context-api-in-python/5684), here a React Context-like API for Python to pass data down in thesub-function without polluting all the function parameters.

Under the hood it uses `inspect.stack().frame` to register the element in the context manager. Frames may be available only in CPython. 

# Define context values

To define a context value use `use_context(**kargws)` function

```

with use_context(something=123):
    ...

```
​
# Retrieve the value somewhere in the code inside of the context

To retrieve the value, use `get_context(key)` function

# Complete example

```
def nested_function():
    return get_context('something', 'default_value')

with use_context(something=123):
    value = nested_function()
    print(value) # 123
print(nested_function()) # 'default_value'
```

# How to debug the context 

To print in the console where a context has been defined in the stacktrace, replace `get_context` with `debug_context(key, logger=print)`

### For the complete implementation and behaviour, please check the [test file](https://github.com/alessandro308/react_context/blob/main/tests/test_react_context.py).

