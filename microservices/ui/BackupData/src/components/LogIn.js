import React from 'react';
import Dialog from 'material-ui/Dialog';
import FlatButton from 'material-ui/FlatButton';
import RaisedButton from 'material-ui/RaisedButton';
//import '../App.css';
import TextField from 'material-ui/TextField';
import {orange500, blue500} from 'material-ui/styles/colors';
import Signup from './Signup' ;
import { Link } from 'react-router-dom';

 var LabelText={
    marginLeft:'0px',
    textTransform: 'capitalize',
    fontSize:'19px',
    color:'white',
  }
  var LabelText2={
    marginLeft:'0px',
    textTransform: 'capitalize',
    fontSize:'13px',
    color:'#1565C0',
  }


const customContentStyle = {
  
  width:'40em',
  position: 'absolute',
  boxSizing: 'border-box',
  WebkitTapHighlightColor: 'rgba(0,0,0,0)', // Remove mobile color flashing (deprecated)
  maxHeight : ' !important  100%',
  top: 0,
  left:20,
  display:'inlineBlock',
  right:0,
  

};
var Bodyst={
     /* backgroundColor:'red', */

}
const styles = {
  errorStyle: {
    color: orange500,
  },
  underlineStyle: {
    borderColor: orange500,
  },
  floatingLabelStyle: {
    color: orange500,
  },
  floatingLabelFocusStyle: {
    color: blue500,
  },
};
var loginBstyle={
  backgroundColor:"orange",
}
var SignupBstyle={
  textTransform:'capitalize',

}

/**
 * Alerts are urgent interruptions, requiring acknowledgement, that inform the user about a situation.
 */
class LogIn extends React.Component {
  
 /* constructor(props) {
    super(props);
    this.state = {
      showComponent: false,
    };
    this._onButtonClick = this._onButtonClick.bind(this);
  }

  _onButtonClick() {
    this.setState({
      showComponent: true,
    });
  }

*/











  state = {
    open: false,
    showComponent: false,
  };

  handleOpen = () => {
    this.setState({open: true});
  };

  handleClose = () => {
    this.setState({open: false});
  };
  _onButtonClick= () => {
    this.setState({showComponent: true});
    
  };

                          

 
 

  render() {
    const actions = [
      <FlatButton
        label="Cancel"
        primary={true}
        onClick={this.handleClose}
      />,
      <FlatButton
        label="Discard"
        primary={true}
        onClick={this.handleClose}
      />,
    ];

    return (
      <div>
        <FlatButton label="Login & Signup" onClick={this.handleOpen}  labelStyle={LabelText}   />
        <Dialog  bodyStyle={Bodyst} paperClassName='Paperstyle'
          actions={actions}
          modal={false}
          open={this.state.open}
          onRequestClose={this.handleClose}
           autoScrollBodyContent={true}
            contentStyle={customContentStyle}
        >
          <div className="mainLoginDiv">
              <div className="loginInImage" width="50%">
                  <div className="LoginText"><h2> LogIn  </h2>  </div>

                  <div className="LoginText">Get access to your Orders, Wishlist and Recommendations</div>


              </div>

              <div className="loginForm" width="50%">
                    <div className="TextForm">
                          <div> <TextField
                              floatingLabelText="Enter E-mail/Mobile number"
                              floatingLabelStyle={styles.floatingLabelStyle}
                              floatingLabelFocusStyle={styles.floatingLabelFocusStyle}
                            />
                         </div>
                             <div>
                                <TextField
                                  floatingLabelText="Enter Password"
                                  floatingLabelStyle={styles.floatingLabelStyle}
                                  floatingLabelFocusStyle={styles.floatingLabelFocusStyle}
                                />
                                </div>
                      <div className="Loginbutton">
                      <div >
                          <FlatButton label="Login" onClick={this.handleOpen}  labelStyle={LabelText} fullWidth={true} style={loginBstyle}   /> 
                        </div>
                                <div className="signupbutton">
                                         <FlatButton onClick={this._onButtonClick} label="New To LIfestyle? " style={SignupBstyle} labelStyle={LabelText2} />
                                {
                                  this.state.showComponent ? <Signup />  : null
                                }
                                 
                   
                                 </div>
                  </div>






                     </div>






              </div>

           

          </div>





          Discard draft?
        </Dialog>
      </div>
    );
  }
}
export default LogIn;