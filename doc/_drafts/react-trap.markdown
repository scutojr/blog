# React


# Trap


## Avoid using "key" in props

"key" is a reserved word in React and it's used by the child of an array.
When you miss this, you will get this annoying Warning:
```
Warning: Each child in an array or iterator should have a unique "key" prop.
```

If you pass "key" to your custom component, it will end up with undefined.
