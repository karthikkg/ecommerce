import React, {Component} from 'react';
import { Redirect } from 'react-router-dom';
import fetch from 'isomorphic-fetch';
import Cookies from 'universal-cookie';

class Logout extends Component{

	removeCookies(){
		const cookies = new Cookies();
		cookies.remove('auth_token', { path: '/' });
		cookies.remove('hasura_id', { path: '/' });
		cookies.remove('username', { path: '/' });

		alert('Logged Out succesfully')
		this.props.history.push("/")
	}
	componentDidMount(){
      this.removeCookies();
    }
	render(){
		
		return(

				<div>{this.removeCookies()} </div>
			);
	}
}
export default Logout;