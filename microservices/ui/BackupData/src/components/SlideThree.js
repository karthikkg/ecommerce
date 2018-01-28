
import React, { Component } from 'react';
import Virat from './Images/S3.jpg';

const SlideThree= (props) => {

  let background = {
     backgroundImage: 'url(' + Virat + ')' ,
    backgroundSize: 'cover',
    backgroundPosition: 'center'
  }

  return <div style={background} className="slide">

   <h1> willson </h1> 
              <h1> S3 </h1>
              <h1> S3 </h1>
              <h1> S3 </h1>
              <h1> S3 </h1>  



  </div>
}

export default SlideThree;
