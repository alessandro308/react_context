
# react_context

An API to pass data down in the sub-function inspired by React Context

```
pip install react-context
```

Inspired by (this reddit)[https://discuss.python.org/t/react-context-api-in-python/5684], here a React Context-like API for Python to pass data down in thesub-function without polluting all the function parameters.

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
    return get_context('something')

with use_context(something=123):
    value = nested_function()
    print(value) # 123
```

# Debug the code

To print in the console where a context has been defined in the stacktrace, replace `get_context` with `debug_context`

### For the complete implementation and behaviour, please check the test file.