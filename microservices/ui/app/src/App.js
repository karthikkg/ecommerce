import React, { Component } from 'react';
import { Switch, Route} from 'react-router-dom';
import Reboot from 'material-ui/Reboot';
import 'typeface-roboto';
import { MuiThemeProvider } from 'material-ui/styles';
import './App.css';
import Product from './components/product';
import Cart from './components/cart';
import Header from './components/header';
import Footer from './components/footer';
import Home from './components/home';
import User from './components/user';
import Auth from './components/auth';
import Login_Signup from './components/Login_Signup.js';
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
                      <Route path="/cart" component={Cart}/>
                      <Route path="/user" component={User}/>
                      <Route path="/auth" component={Login_Signup}/>
                      <Route path="/product/:productId" component={Product}/>
                      <Route path="/logoutRedirec" component={LogoutRedirec}/>
                </Switch>
                <Footer/>
            </MuiThemeProvider>
      </div>        
    );
  }
}
export default App;
