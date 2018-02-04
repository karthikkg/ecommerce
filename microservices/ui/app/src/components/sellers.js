
import React from 'react';
import {Link} from 'react-router-dom';
import GridList, { GridListTile } from 'material-ui/GridList';
import TextField from 'material-ui/TextField';
import Button from 'material-ui/Button';
import Hidden from 'material-ui/Hidden';
import {saveOffline } from './config';
import {authenticateUser, Userinfo, MakeUser} from './api';
import ELlikartLogo from './ElikartLogo.png';
import './Login_Signup.css';
export default class Sellers extends React.Component{
	constructor() {
		super()
		this.state = {
		  username: '',
		  password: '',
			email:'',
			phonenumber:'',
		  firstname:'',
			lastname:'',
		};
		}
	  handleUsernameChange = (e) => {
		this.setState({
		  ...this.state,
		  username: e.target.value
		});
	  }
	  handlePasswordChange = (e) => {
		this.setState({
		  ...this.state,
		  password: e.target.value
		});
	  }
	  handleEmailChange = (e) => {
		this.setState({
		  ...this.state,
		  email: e.target.value
		});
	  }
	  handleFirstnameChange = (e) => {
		this.setState({
		  ...this.state,
		  firstname: e.target.value
		});
		}
		handlePhonenumChange = (e) => {
			this.setState({
				...this.state,
				phonenumber: e.target.value
			});
			}
	  handleLastnameChange = (e) => {
		this.setState({
		  ...this.state,
		  lastname: e.target.value
		});
		} 

		login = () => {
			console.log('on login clicked');
			authenticateUser(this.state.username, this.state.password, false).then(authResponse => {
				console.log(authResponse);
				if (authResponse.auth_token) {
					//Save the auth token offline to be used by the filestore service
					saveOffline(authResponse.auth_token)
					Userinfo().then(Userinfo => {
						console.log(JSON.stringify(Userinfo))
					});
				} else {
					console.log(JSON.stringify(authResponse));
				}
			});
		}
	
		register = () => {
			console.log('on register clicked');
			authenticateUser(this.state.username, this.state.password, true).then(authResponse => {
				console.log(authResponse);
				if (authResponse.auth_token) {
					saveOffline(authResponse.auth_token)
					MakeUser(authResponse.hasura_id,this.state.lastname,this.state.email,this.state.phonenumber,this.state.firstname).then(userres=>{
						console.log(JSON.stringify(userres))
					})
					console.log("SignUp Successful! \n Your auth credentials are: " + JSON.stringify(authResponse, null, 2))
				} else {
					console.log(JSON.stringify(authResponse));
				}
			});
		}
	render(){
		return(
			<div className="Login_Signup_body">
				<Hidden mdDown>
				<GridList cols={2} cellHeight={800}>
					<GridListTile cols={1} className="loginGrid">
                                    <Link to='/auth' params={{ role:"sellers"}}>
                                        <h4>Not a registered seller yet??? Come Here..</h4>
									</Link>
									<div className="center">
										<img src={ELlikartLogo} className="responsive-img" alt="Elikart Logo "/>
									</div>
									<TextField id="Username"
										onChange={this.handleUsernameChange}
										required
										className="textField"
										placeholder="Username / Email"
									/>
									<TextField id="Password"
										onChange={this.handlePasswordChange}
										placeholder="password"
										type="password"
										className="textField"
										autoComplete="current-password"
										required
									/>
								<br/>
								<br/>
								<Button 
									raised 
									color="secondary" 
									onClick= {(e) => {this.login()}}
									>
									Login
								</Button>
					
					</GridListTile>
					<GridListTile cols={1} className="loginGrid">
						<h5>New to Elikart? SignUp below </h5>
						<GridListTile>
							<TextField id="Firstname"
								onChange={this.handleFirstnameChange}
								required
								className="textField"
								placeholder="Firstname"
								/>
							<TextField id="Lastname"
								onChange={this.handleLastnameChange}
								className="textField"
								required
								placeholder="Lastname"
							/>
							<TextField id="Uname"
								onChange={this.handleUsernameChange}	
								className="textField"
								required
								placeholder="Username"
							/>
							<TextField id="email"
								onChange={this.handleEmailChange}
								className="textField"
								required
								placeholder="email"
							/>
							<TextField id="Password"
								onChange={this.handlePasswordChange}
								className="textField"
								placeholder="password"
								type="password"
								required
							/>
							<TextField id="ConfirmPassword"
								onChange={this.handlePasswordChange}
								className="textField"
								placeholder=" confirm password"
								type="password"
								required
							/>
							<TextField id="mobile_no"
								onChange={this.handlePhonenumChange}
								className="textField"
								required
								placeholder="Mobile Number"
							/>
							<br/>   
							<br/>  
							<Button 
								onClick= {(e) => {this.register()}}
								raised 
								color="secondary" 
								>
								SignUp
							</Button>
						</GridListTile>
					</GridListTile>
				</GridList>
				</Hidden>
				<div className="mobileForm">
					<Hidden mdUp>
						<div className="center">
							<img src={ELlikartLogo} className="responsive-img" alt="Elikart Logo "/>
						</div>
						<TextField id="Username"
										onChange={this.handleUsernameChange}
										required
										className="textField"
										placeholder="Username / Email"
									/>
									<TextField id="Password"
										onChange={this.handlePasswordChange}
										placeholder="password"
										type="password"
										className="textField"
										autoComplete="current-password"
										required
									/>
								<br/>
								<br/>
								<Button 
									raised 
									color="secondary" 
									onClick= {(e) => {this.login()}}
									>
									Login
								</Button>
						<br/>
						<h5>New to Elikart? SignUp below </h5>
						<br/>
						<TextField id="Firstname"
								onChange={this.handleFirstnameChange}
								required
								className="textField"
								placeholder="Firstname"
								/>
							<TextField id="Lastname"
								onChange={this.handleLastnameChange}
								className="textField"
								required
								placeholder="Lastname"
							/>
							<TextField id="Uname"
								onChange={this.handleUsernameChange}	
								className="textField"
								required
								placeholder="Username"
							/>
							<TextField id="email"
								onChange={this.handleEmailChange}
								className="textField"
								required
								placeholder="email"
							/>
							<TextField id="Password"
								onChange={this.handlePasswordChange}
								className="textField"
								placeholder="password"
								type="password"
								required
							/>
							<TextField id="ConfirmPassword"
								onChange={this.handlePasswordChange}
								className="textField"
								placeholder=" confirm password"
								type="password"
								required
							/>
							<TextField id="mobile_no"
								onChange={this.handlePhonenumChange}
								className="textField"
								required
								placeholder="Mobile Number"
							/>
							<br/>   
							<br/>  
							<Button 
								onClick= {(e) => {this.register()}}
								raised 
								color="secondary" 
								>
								SignUp
							</Button>			
					</Hidden>
				</div>

			</div>
			
			);
	}
}
