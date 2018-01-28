import React from 'react';
import {GridList,GridTile} from 'material-ui/GridList';
import TextField from 'material-ui/TextField';
import Button from 'material-ui/Button';
import Divider from 'material-ui/Divider';
import FinalLogo2 from './FinalLogo2.png';
import './Login_Signup.css';
class Auth extends React.Component{
	render(){
		return(
			<div className="Login_Signup_body">
			<GridList cols={2}  cellHeight={800}>
			
			<GridTile cols={1}>
			<img className="logo"
			 src={FinalLogo2}/>
			<br/>
			
			<TextField 
			hintText="Email/Username"
			/>
			<br/>
			<TextField
			hintText="Password"
			type="password"
			errorText="This is a required field" />
			<br/><br/>
			<Divider/>
			<br/>
			<Button label="Login" />
			
			</GridTile>

			<GridTile cols={1}>
			<div className="RightPane">
			<h2 className="text">New to Elikart?Sign Up below</h2>
			<TextField
			hintText="FirstName"
			/>
			<br/>
			<TextField
			hintText="LastName"
			/><br/>
			<TextField
			hintText="Username"
			errorText="This is a required field"
			/><br />
			<TextField
			hintText="valid email id"
			errorText="This is a required field"
			/><br />
			<TextField
      		hintText="Password"
      		type="password"
      		errorText="This is a required field"
    		/><br />
    		<TextField
      		hintText="Confirm Password"
      		type="password"
      		errorText="This is a required field"
    		/>
    		<br /><br/>
    		<Divider />
    		<br/>
    		<Button label="Sign Up"/>
    		<br/>
    		</div>
    		</GridTile>
			
			
			</GridList>
			</div>
			);
	}
}
export default Auth;