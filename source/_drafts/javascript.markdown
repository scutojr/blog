---
title: javascript
categories: []
---

# Content

- project directory structure
- webpack skill 


# JsonRpc client on JavaScript

**key words**: promise, es6




# Nginx for delegation

# Promise

promise.then method return a new promise

# Cross-Origin

> [Cross-origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS)

New standard for cross-origin access.

**simple request**

request headers: Origin: http://foo.example

response headers:
- Access-Control-Allow-Origin: *
- Access-Control-Allow-Origin: http://bar.other


# React

I think state is only used for web interactive data and making change of the data.
I think props is only used for 


# Javascript

**Deep Copy a Object**

Convert the JavaScript object into a JSON string, then convert it back into a JavaScript object.
```
JSON.parse(JSON.stringify(o))
```

## Set

new Set(<Iterable>)

## Array

**Merge two arrays**
```
const arr1 = [1,2]
const arr2 = [3, 4]
const arr3 = [...arr1, ...arr2]
```

---

# Project Directory Structure

- use index.js to organize the package so that import from other package only need to know the package name
instead of the other file under this package. just like __init__.py in python


---

# Webpack Skill 

**build for production and test environment as following:**
```
$ yarn build:dev
$ yarn build:prod
```

**package.json**
```
{
  "name": "app1",
  "version": "1.0.0",
  "description": "test yarn tool",
  "main": "index.js",
  "author": "oujianrong",
  "license": "MIT",
  "scripts": {
    "build": "webpack --config webpack.config.dev.js",
    "build:dev": "webpack --config webpack.config.dev.js",
    "build:prod": "webpack --config webpack.config.prod.js",
    "start": "webpack-dev-server --host 0.0.0.0 --port 8080 --config webpack.config.dev.js --progress --colors"
  },
  "dependencies": {
    "assert": "^1.4.1",
    "babel-preset-es2017": "^6.24.1",
    "babel-preset-stage-0": "^6.24.1",
    "baobab": "^2.5.0",
    "bundle": "^0.2.3",
    "chance": "^1.0.12",
    "namor": "^1.0.1",
    "node-sass": "^4.7.2",
    "path": "^0.12.7",
    "prop-types": "^15.6.0",
    "react": "^16.0.0",
    "react-bootstrap": "^0.31.3",
    "react-bootstrap-table": "^4.1.5",
    "react-dom": "^16.0.0",
    "react-responsive-modal": "^2.0.0",
    "react-router": "^4.2.0",
    "react-router-dom": "^4.2.2",
    "react-treeview-component": "^0.1.2",
    "sass-loader": "^6.0.6",
    "url-loader": "^0.6.2",
    "webpack": "^3.10.0",
    "webpack-dev-server": "^2.9.1"
  },
  "devDependencies": {
    "babel-core": "^6.26.0",
    "babel-loader": "^7.1.2",
    "babel-preset-es2015": "^6.24.1",
    "babel-preset-react": "^6.24.1"
  }
}
```

**webpack.config.dev.js**
```
var path = require('path');
var webpack = require('webpack')

var isProduction = false

var define = new webpack.DefinePlugin({
    PRODUCTION: JSON.stringify(isProduction),
    DEVELOPMENT: JSON.stringify(!isProduction)
})

module.exports = {
    devtool: 'eval',
    entry: [
        path.resolve(__dirname, './app/main.js')
    ],
    output: {
        path: path.resolve(__dirname, './build'),
        filename: 'bundle.js'
    },
    module: {
        loaders: [
            { test: /\.js$/, loader: 'babel-loader', exclude: /node_modules/ },
            { test: /\.jsx$/, loader: 'babel-loader', exclude: /node_modules/ },
        ]
    },
    plugins: [
        define
    ],
    devServer: {
        contentBase: "./build",
        historyApiFallback: true,
        inline: true
    }
}
```

variable **PRODUCTION** and **DEVELOPMENT** can be used directly in the js code, webpack will
replace it with the proper value on compiling.


# Reference

> [Web API](https://developer.mozilla.org/en-US/docs/Web/API)
> [Web technology for developers](https://developer.mozilla.org/en-US/docs/Web)





# Example


**show or hide a div**
```

class EventEntry extends React.Component {
    constructor({ group }) {
        super({ group })
        this.state = {
            visible: false
        }
    }

    render() {
        let group = this.props.group
        let id = group._id
        let tags = []
        let latest = 0, status = 'ok'
        group.events.forEach((ele) => {
            if (ele.start_at > latest) {
                latest = ele.start_at
                status = ele.status
            }
        })
        for (let [key, value] of Object.entries(id.tags)) {
            tags.push(`${key}=${value}`)
        }
        const style = {
            display: this.state.visible ? "block" : "none"
        };
        var header = `${id.event_name}    ${tags.join(",")}    ${id.endpoint}`
        return (
            <Panel header={header} id={header} bsStyle={status == "ok" ? "success" : "danger"}>
                <div style={style}>
                    <EventTable events={group.events} />
                </div>
            </Panel>
        )
    }
}
```
