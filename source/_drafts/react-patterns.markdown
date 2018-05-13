---
title: react pattern
categories: []
---

# Content

- react pattern


# Philosophy

React philosophy is that props should be immutable and top-down.


# React Pitfall

react仅仅是Dom层面的抽象， 缺少代码组织和组件间通信。 react通过props维持data flow


# Pattern

```
                     +-------------------------+
                     |                         |
                     |   Container Component   |
                     |                         |
                     +------+----------^-------+
                            |          |
   stateful                 |          |                behavioural layer
                            |          |
====================      props     callback       ===========================
                            |          |
   stateless                |          |                presentational layer
                            |          |
                            |          |
                     +------v----------+-------+
                     |                         |
                     |       Components        |
                     |                         |
                     +-------------------------+

```

## Proxy Component

Wrap a component with some default properties and style.


Say we have a button. It uses classes to be styled as a "primary" button.
```
<button type="button" className="btn btn-primary">
```

We can generate this output using a couple single-purpose components.
```
import classnames from 'classnames'

const PrimaryBtn = props =>
  <Btn {...props} primary />

const Btn = ({ className, primary, ...props }) =>
  <button
    type="button"
    className={classnames(
      "btn",
      primary && "btn-primary",
      className
    )}
    {...props}
  />
```

It can help to visualize this.
```
PrimaryBtn()
  ↳ Btn({primary: true})
    ↳ Button({className: "btn btn-primary"}, type: "button"})
      ↳ '<button type="button" class="btn btn-primary"></button>'
```

Using these components, all of these result in the same output.
```
<PrimaryBtn />
<Btn primary />
<button type="button" className="btn btn-primary" />
```

This can be a huge boon to style maintenance. It isolates all concerns of style to a single component.


## Layout Component

Just as its name implies, it's a component used to control layout. It might not need to update
frequently and it accepts dom element from its props.
```
class HorizontalSplit extends React.Component {
  shouldComponentUpdate() {
    return false
  }

  render() {
    <FlexContainer>
      <div>{this.props.leftSide}</div>
      <div>{this.props.rightSide}</div>
    </FlexContainer>
  }
}
```


## Container component

A container does data fetching and then renders its corresponding sub-component.

```
class TableContainer extends React.Component {
  constructor() {
    super()
    this.state = { comments: [] }
  }

  componentDidMount() {
    // fetch data here
    $.ajax({
        ...
        this.setState(...);
    })
  }

  render() {
    return (
        <Table>
            // fill the table with data
        </Table>
    )
  }
}
```


## Higher-order component

A [higher-order component](https://reactjs.org/docs/higher-order-components.html) is a function
that takes a component, wrap it and return a new component


## Stateless Component

You can use either a function or a class for creating stateless components.

You should go for stateless functional components unless you need to use a lifecycle hook in your components.

Benfits of stateless functional components:
- easy to write, understand, and test
- avoid the this keyword


Pitfall of stateless functional components:
- don't have lifecycle hooks such as **ShouldComponentUpdate()**


## Stateful Component

Stateful components are always class components and  have a state that gets initialized in the constructor. 

```
class App extends Component {
   
  /*
  // Not required anymore
  constructor() {
      super();
      this.state = {
        count: 1
      }
  }
  */
   
  state = { count: 1 };
   
  handleCount(value) {
      this.setState((prevState) => ({count: prevState.count+value}));
  }
 
  render() {
    // omitted for brevity
  }
   
}
 
```


# Organization

- code organization inside js file of es6
- directory structure for components


## Code organization

[Example](https://github.com/react-bootstrap/react-bootstrap/blob/master/src/Image.js#L28)
```
+------------------------+
|                        |
|                        |
|  PropTypes Definition  |
|                        |
|                        |
+------------------------+
|                        |
|                        |
|  Default Props Value   |
|                        |
|                        |
+------------------------+
|                        |
|                        |
|  Class Definition      |
|                        |
|                        |
+------------------------+
|                        |
|  Class static member   |
|  such as propTypes     |
|  and defaultProps      |
|                        |
+------------------------+
```

Convention to organzie react code?

```
 
  [典型component代码结构](https://github.com/react-bootstrap/react-bootstrap/blob/master/src/Image.js#L28)
   
    
     https://github.com/react-bootstrap/react-bootstrap/blob/master/src/FormGroup.js
      
       
        react-bootstrap的代码组织以及 index.js的作用
```


# Related Framework

Redux

Flux


# Reference

https://code.tutsplus.com/tutorials/stateful-vs-stateless-functional-components-in-react--cms-29541

https://github.com/chantastic/reactpatterns.com

https://github.com/AllenFang/react-bootstrap-table
