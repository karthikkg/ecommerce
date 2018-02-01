import React,{ Component } from 'react';
import {Link} from 'react-router-dom';
import Hidden from 'material-ui/Hidden';
import BottomNavigation, { BottomNavigationAction } from 'material-ui/BottomNavigation';
import {Home, VerifiedUser, Check,Clear } from 'material-ui-icons';

export default class Footer extends Component{
  
  state = {

    value: 'home',
  };

  handleChange = (event, value) => {
    this.setState({ value });
  };


  render(){
  return(
    <div>
      <Hidden mdUp>  
        <BottomNavigation  className="footer" showLabels={true} value = {this.state.value} onChange={this.handleChange}>
          <Link to="/"><BottomNavigationAction label="home" value="home" icon={<Home />}/></Link>
          <Link to="/user"><BottomNavigationAction label="User" value="user" icon={<VerifiedUser />}/></Link>
          <Link to ="/auth"><BottomNavigationAction label="Cart" value="cart" icon={<Check />} /></Link>
          <Link to ="/logoutRedirec"><BottomNavigationAction label="Logout" value="logout" icon={<Clear />} /></Link>
        </BottomNavigation>       
      </Hidden> 
  </div>
 )
}
}