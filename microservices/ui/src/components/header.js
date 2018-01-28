import React,{ Component } from 'react';
import {Link} from 'react-router-dom';
import Hidden from 'material-ui/Hidden';
import BottomNavigation, { BottomNavigationAction } from 'material-ui/BottomNavigation';
import {Home, VerifiedUser, Check,Clear } from 'material-ui-icons';

export default class Header extends Component{
  
  state = {
    value: 'home',
  };

  handleChange = (event, value) => {
    this.setState({ value });
  };


  render(){
  return(
    <div>
    <nav>
      <div class="nav-wrapper">
        <a href="#!" class="brand-logo"><Link to="/">EliKart</Link></a>
        <ul class="right hide-on-med-and-down">
                <li><Link to="/">Home</Link></li>
                <li><Link to="/user">User</Link></li>
                <li><Link to ="/auth">Login/SingUp</Link></li>
                <li><Link to ="/logoutRedirec">LogOut</Link></li>
        </ul>
      </div>
    </nav> 
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