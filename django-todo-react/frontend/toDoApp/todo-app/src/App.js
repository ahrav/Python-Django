import React, { Suspense } from "react"
import { BrowserRouter, Route, Switch, Redirect } from 'react-router-dom';


const Todo = React.lazy(() => {
  return import('./components/Todo/Todo.js')
})

const Auth = React.lazy(() => {
  return import('./containers/Auth/Auth.js')
})

const App = props => {
  
  let routes = (
    <BrowserRouter>
      <Switch>
        <Route path="/todos" component={Todo}/>
        <Route path="/" exact component={Auth}/>
        <Redirect to="/"/>
      </Switch>
    </BrowserRouter>
  )
  return (
    <React.Fragment>
      <Suspense fallback={<h1>Loading...</h1>}>
        {routes}
      </Suspense>
    </React.Fragment>
  )
}

export default App