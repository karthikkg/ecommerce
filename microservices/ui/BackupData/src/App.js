import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import Toolbar2 from './components/Toolbar2' ;
import AutoCom from './components/Autocom' ;
import CategoryBar from './components/CategoryBar' ;
import Slider from './components/Slider' ;
//import MyLog from './components/MyLog' ;
import LogIn from './components/LogIn' ;
//import Carousel  from './components/Carousel' ;
//import Paper1 from './components/Paper1' ;



     class App extends Component {
      render() {
      return (
        <MuiThemeProvider>
       <div className="App">
          <Toolbar2/>
          <CategoryBar/>
          
        
        
        <Slider/> 
     

        </div>
        </MuiThemeProvider>
               );
          }
         }
                         /*const app=document.getElementById('root')
                               ReactDom.render(<Layout/>,app);
                          */
export default App;
