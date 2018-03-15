import React, { Component } from 'react';
import { Switch, Route} from 'react-router-dom';



import Home from './components/home.js';
import Login from './components/login.js';
import Header from './components/header.js';
import AddProduct from './components/addProduct.js';
import Search from './components/search.js';
import Logout from './components/logout.js';
import Product from './components/product';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
              <Header/>
                 <Switch>
                      <Route exact path="/" component={Home}/>
                      <Route exact path="/search" component={Search}/>
                      <Route path="/addProduct" component={AddProduct}/>
                      <Route path="/login" component={Login}/>
                      <Route path="/product/:productId" component={Product}/>
                      
                      
                </Switch>
            
      </div>        
    );
  }
}
export default App;
