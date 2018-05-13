---
title: react trap
categories: []
---

# React


# Trap


## Avoid using "key" in props

"key" is a reserved word in React and it's used by the child of an array.
When you miss this, you will get this annoying Warning:
```
Warning: Each child in an array or iterator should have a unique "key" prop.
```

If you pass "key" to your custom component, it will end up with undefined.


## Let recreating component

if we want to let "defaultValue" and "defaultChecked" take effect everytime
we re-render the input component:
```
<div key="key to tell React to recreate the component">
    <input/>
</div>
```


## Props and State

I think use props is better

TODO: when should we use state?


## About input

checkbox properties:
```
1. checked: true of false
2. value: please forget it because it's always "on" and can't update how it looks like by mouse click
3. defaultChecked: like checked, but only takes effect the first it's mounted
```

