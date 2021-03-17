import React from 'react';
import {Switch, Route} from 'react-router-dom'
import './scss/style.scss';
import { CFade } from '@coreui/react'
const loading = (
  <div className="pt-3 text-center">
    <div className="sk-spinner sk-spinner-pulse"></div>
  </div>
)

const TheLayout = React.lazy(() => import('./containers/TheLayout'));
const Login = React.lazy(() => import('./views/pages/login/Login'));
const Register = React.lazy(() => import('./views/pages/register/Register'));
const Page404 = React.lazy(() => import('./views/pages/page404/Page404'));
const Page500 = React.lazy(() => import('./views/pages/page500/Page500'));
const Test = React.lazy(() => import('./views/pages/Test'))
function App() {
  
  return (
    <>
      <React.Suspense fallback={loading}>
        <Switch>
          <Route exact path="/test" name="test" render={props => <Test {...props}/>} />
          <Route exact path="/login" name="Login Page" render={props => <CFade><Login {...props}/></CFade>} />
          <Route exact path="/register" name="Register Page" render={props => <CFade><Register {...props}/></CFade>} />
          <Route exact path="/404" name="Page 404" render={props => <Page404 {...props}/>} />
          <Route exact path="/500" name="Page 500" render={props => <Page500 {...props}/>} />
          <Route path="/" name="Home" render={props => <TheLayout {...props}/>} />
        </Switch>
      </React.Suspense>
    </>
  )
}

export default App;
