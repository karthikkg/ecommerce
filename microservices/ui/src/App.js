import React, { Component } from 'react';
import { Switch, Route} from 'react-router-dom';
import Reboot from 'material-ui/Reboot';
import 'typeface-roboto';
import { MuiThemeProvider } from 'material-ui/styles';
import './App.css';
import Header from './components/header';
import Home from './components/home';
import User from './components/user';
import Auth from './components/auth';
import LogoutRedirec from './components/logoutRedirec';

class App extends Component {
  render() {
    return (
      <div className="App">
          <MuiThemeProvider>
              <Reboot />
              <Header/>
                 <Switch>
                      <Route exact path="/" component={Home}/>
                      <Route path="/user" component={User}/>
                      <Route path="/auth" component={Auth}/>
                      <Route path="/logoutRedirec" component={LogoutRedirec}/>
                </Switch>
            </MuiThemeProvider>
      </div>        
    );
  }
}
export default App;
