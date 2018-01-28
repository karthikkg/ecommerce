
import React, { Component } from 'react';
import Virat from './Images/S1.jpg';

const SlideOne= (props) => {

  let background = {
    backgroundImage: 'url(' + Virat + ')' ,
    backgroundSize: 'cover',
    backgroundPosition: 'center',
     
  }

  return <div style={background}  className="slide">
              <h1> willson </h1> 
              <h1> willson </h1>
              <h1> willson </h1>
              <h1> willson </h1>
              <h1> willson </h1>  

  </div>
}

export default SlideOne;
