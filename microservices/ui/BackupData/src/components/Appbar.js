import React from 'react';

import AppBar from 'material-ui/AppBar';
import IconButton from 'material-ui/IconButton';
import FontIcon from 'material-ui/FontIcon';
import FlatButton from 'material-ui/FlatButton';
import '../App.css';
import {blue500} from 'material-ui/styles/colors';
import cyan500 from 'material-ui/styles/colors';


import Searchbar from './Searchbar';
import '../App.css';

/**
 * A simple example of `AppBar` with an icon on the right.
 * By default, the left icon is a navigation-menu.
 */


  var buttonStyle = {
     backgroundColor: 'white',
      color: 'blue'
    }
    var buttonStyle2 = {
       backgroundColor: '#29B6F6',
     borderRadius:50
      }
      var LabelTextTweet={
        textTransform: 'capitalize',
        color:'#FFFFFF',
      }
      var LabelText={
        textTransform: 'capitalize',
        color:'#616161',
        fontWeight:'bold',
      }
     


   var rightButtons = (
     <div>



            <IconButton tooltip="Profile and Settings">
                <FontIcon className="fa fa-user-circle-o" aria-hidden="true" />
                 
               </IconButton>

            <FlatButton label="Tweet"  style={buttonStyle2}   labelStyle={ LabelTextTweet}  />

      </div>
    );

      const leftButtons = (
        <div>

              <FlatButton label="Home" style={buttonStyle} labelStyle={LabelText}
                                icon={<i class="fa fa-home" aria-hidden="true"></i>}
                />
               <FlatButton label="Notifications" style={buttonStyle} labelStyle={LabelText}
                                                icon={  <i class="fa fa-bell-o" aria-hidden="true"></i>}
                 />
               <FlatButton label="Messages"  hoverColor={blue500} style={buttonStyle} labelStyle={LabelText}
                                            icon= {<i class="fa fa-envelope-o" aria-hidden="true"></i>}
                />
               <i class="fa fa-twitter fa-2x" style={{fontSize:'25px' ,color:'#29B6F6',marginTop:'3px' }}></i>
            <Searchbar/>
         </div>
      );


const Appbar = () => (
  <AppBar

    title="Twitter"
    iconClassNameRight="muidocs-icon-navigation-expand-more"
        className="home"
         iconElementLeft={leftButtons}
         iconElementRight={rightButtons}

          style={{backgroundColor:cyan500, }} //for setting the Appbar Backgrund color



  />

);

export default Appbar;
