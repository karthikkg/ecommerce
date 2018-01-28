
import React, { Component } from 'react';
import Virat from './Images/S2.jpg';

const SlideTwo= (props) => {

  let background = {
 backgroundImage: 'url(' + Virat + ')' ,
    backgroundSize: 'cover',
    backgroundPosition: 'center'
  }

  return <div style={background} className="slide"> 
              <h1> S2 </h1>
              <h1> S2 </h1>
              <h1> S2 </h1>
             <h1> S2 </h1>
             <h1> S2 </h1> 
              




  </div>
}

export default SlideTwo;
