import React,{ Component } from 'react';
import {Link} from 'react-router-dom';
import Hidden from 'material-ui/Hidden';
import BottomNavigation, { BottomNavigationAction } from 'material-ui/BottomNavigation';
import {Home, VerifiedUser, Check,Clear } from 'material-ui-icons';
import BrandLogoElikart from './brandLogoElikart.png';

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
      <div class="nav-wrapper deep-purple accent-2">
        <Link to="/"><img src={BrandLogoElikart} alt="Brand Logo ELikart" className="left brand-logo"/></Link>
        <ul class="right hide-on-med-and-down">
                <li><Link to="/">Home</Link></li>
                <li><Link to="/user">User</Link></li>
                <li><Link to ="/auth">Login/SignUp</Link></li>
                <li><Link to ="/logoutRedirec">LogOut</Link></li>
        </ul>
      </div>
    </nav> 
  </div>
 )
}
}