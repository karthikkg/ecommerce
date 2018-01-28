import React from 'react';
import Dialog from 'material-ui/Dialog';
import FlatButton from 'material-ui/FlatButton';
import RaisedButton from 'material-ui/RaisedButton';
//import '../App.css';
import TextField from 'material-ui/TextField';
import {orange500, blue500} from 'material-ui/styles/colors';

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
  zDepth:'5',
}
var SignUpbstyle={
  backgroundColor:"blue",
}

/**
 * Alerts are urgent interruptions, requiring acknowledgement, that inform the user about a situation.
 */
class Signup extends React.Component {
  state = {
    open: false,
  };

  handleOpen = () => {
    this.setState({open: true});
  };

  handleClose = () => {
    this.setState({open: false});
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
        <FlatButton label="Signup" onClick={this.handleOpen} style={SignUpbstyle} labelStyle={LabelText}   className="signupbutton"/>
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
                  <div className="LoginText"><h2> Sign up </h2>  </div>

                  <div className="LoginText">We do not share your personal details with anyone</div>


              </div>

              <div className="loginForm" width="50%">
                    <div className="TextForm">
                          <div> <TextField
                              floatingLabelText="Enter Mobile number"
                              floatingLabelStyle={styles.floatingLabelStyle}
                              floatingLabelFocusStyle={styles.floatingLabelFocusStyle}
                            />
                         </div>
                            
                      <div className="Loginbutton">
                      <div >
                          <FlatButton label="Sign Up" onClick={this.handleOpen}  labelStyle={LabelText} fullWidth={true} style={loginBstyle}   /> 
                        </div>
                        <div className="signupbutton">
                          <FlatButton label="Extisting User?Log in" onClick={this.handleOpen}  labelStyle={LabelText2} fullWidth={true} style={SignupBstyle}  /> 
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
export default Signup;