import React from 'react';
import IconMenu from 'material-ui/IconMenu';
import IconButton from 'material-ui/IconButton';
import FontIcon from 'material-ui/FontIcon';
import FlatButton from 'material-ui/FlatButton';
import {Toolbar, ToolbarGroup} from 'material-ui/Toolbar';
import '../App.css';
import MoreVertIcon from 'material-ui/svg-icons/navigation/more-vert';

import ActionAndroid from 'material-ui/svg-icons/action/android';
import Searchbar from './Searchbar';
import LogIn from './LogIn' ;
import RaisedButton from 'material-ui/RaisedButton';
import DropDownMenu from 'material-ui/DropDownMenu';
import MenuItem from 'material-ui/MenuItem';
import ContentFilter from 'material-ui/svg-icons/content/filter-list';



var buttonStyle2={
 borderBottom:'1px solid #00BCD4',
}

var buttonStyle={
       backgroundColor:'#1565C0',


}
  var ToolbarStyle={
        backgroundColor:'#1565C0',

}
  var LabelText={
    marginLeft:'0px',
    textTransform: 'capitalize',
    fontSize:'19px',
    color:'white',
  }


export default class Toolbar2 extends React.Component {


  constructor(props) {
    super(props);
    this.state = {
      value: 3,
    };
  }

  handleChange = (event, index, value) => this.setState({value});

  render() {
    return (
      <Toolbar style={ToolbarStyle} >
        <ToolbarGroup firstChild={false}>
        <span className="TopButton">  <FlatButton label="Lifestyle" style={buttonStyle2}  labelStyle={LabelText}  icon={<ActionAndroid/>} /></span>
      <span>  <Searchbar/></span>
</ToolbarGroup>

<ToolbarGroup>


         <LogIn />

              <div class="dropdown">
        <button class="dropbtn">More
          <i class="fa fa-caret-down"></i>
        </button>
        <div class="dropdown-content">
          <a href="#">Sell on Lifestyle</a>
          <a href="#">24*7 Helpline</a>
          <a href="#">Advertise With us</a>
        </div>
        </div>








        <span>  <FlatButton  label="Cart"  style={buttonStyle} labelStyle={LabelText}
            icon={<i class="fa fa-shopping-cart fa-lg" aria-hidden="true" style={{color:'white' }} fa-lg></i> }

          />
          </span>

        </ToolbarGroup>
      </Toolbar>
    );
  }
}
