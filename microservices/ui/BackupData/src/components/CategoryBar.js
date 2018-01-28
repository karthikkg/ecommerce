import React from 'react';
import {Tabs, Tab} from 'material-ui/Tabs';
import FontIcon from 'material-ui/FontIcon';
import MapsPersonPin from 'material-ui/svg-icons/maps/person-pin';
import '../App.css';

var IconStyle={
  float:'right',
  verticleAlign:'bootom',


}


const CategoryBar = () => (
  <div class="navbar">


  <div class="dropdown">
      <button class="dropbtn"> Electronics
        <i class="fa fa-caret-down"></i>
      </button>
    <div class="dropdown-content">

                    <div class="row">
                                  <div class="column">
                                    <h3>Mobiles</h3>
                                    <a href="#">Link 1</a>
                                    <a href="#">Link 2</a>
                                    <a href="#">Link 3</a>
                                  </div>
                                  <div class="column">
                                    <h3>Laptops</h3>
                                    <a href="#">Link 1</a>
                                    <a href="#">Link 2</a>
                                    <a href="#">Link 3</a>
                                  </div>
                                  <div class="column">
                                    <h3>Television</h3>
                                    <a href="#">Link 1</a>
                                    <a href="#">Link 2</a>
                                    <a href="#">Link 3</a>
                                  </div>
                    </div>
    </div>
  </div>




<div class="dropdown">
      <button class="dropbtn">Appliances
        <i class="fa fa-caret-down"></i>
      </button>
  <div class="dropdown-content">

                      <div class="row">
                        <div class="column">
                          <h3>Television</h3>
                          <a href="#">Link 1</a>
                          <a href="#">Link 2</a>
                          <a href="#">Link 3</a>
                        </div>
                        <div class="column">
                          <h3>Washing Machine</h3>
                          <a href="#">Link 1</a>
                          <a href="#">Link 2</a>
                          <a href="#">Link 3</a>
                        </div>
                        <div class="column">
                          <h3>Kitchen Appliances</h3>
                          <a href="#">Link 1</a>
                          <a href="#">Link 2</a>
                          <a href="#">Link 3</a>
                        </div>
                    </div>
</div>
</div>


<div class="dropdown">
      <button class="dropbtn">Mens
        <i class="fa fa-caret-down"></i>
      </button>
  <div class="dropdown-content">

                      <div class="row">
                        <div class="column">
                          <h3>Foot Wear</h3>
                          <a href="#">Link 1</a>
                          <a href="#">Link 2</a>
                          <a href="#">Link 3</a>
                        </div>
                        <div class="column">
                          <h3>Top Wear</h3>
                          <a href="#">Link 1</a>
                          <a href="#">Link 2</a>
                          <a href="#">Link 3</a>
                        </div>
                        <div class="column">
                          <h3>Sports Wear</h3>
                          <a href="#">Link 1</a>
                          <a href="#">Link 2</a>
                          <a href="#">Link 3</a>
                        </div>
                    </div>
</div>
</div>

<div class="dropdown">
      <button class="dropbtn">Women
        <i class="fa fa-caret-down"></i>
      </button>
  <div class="dropdown-content">

                      <div class="row">
                        <div class="column">
                          <h3>Clothing</h3>
                          <a href="#">Link 1</a>
                          <a href="#">Link 2</a>
                          <a href="#">Link 3</a>
                        </div>
                        <div class="column">
                          <h3>Ethinc wear</h3>
                          <a href="#">Link 1</a>
                          <a href="#">Link 2</a>
                          <a href="#">Link 3</a>
                        </div>
                        <div class="column">
                          <h3>Footwear</h3>
                          <a href="#">Link 1</a>
                          <a href="#">Link 2</a>
                          <a href="#">Link 3</a>
                        </div>
                    </div>
</div>
</div>



<div class="dropdown">
      <button class="dropbtn">Baby & kids
        <i class="fa fa-caret-down"></i>
      </button>
  <div class="dropdown-content">

                      <div class="row">
                        <div class="column">
                          <h3>kids Clothing</h3>
                          <a href="#">Link 1</a>
                          <a href="#">Link 2</a>
                          <a href="#">Link 3</a>
                        </div>
                        <div class="column">
                          <h3>Kids Footwear</h3>
                          <a href="#">Link 1</a>
                          <a href="#">Link 2</a>
                          <a href="#">Link 3</a>
                        </div>
                        <div class="column">
                          <h3>Toys</h3>
                          <a href="#">Link 1</a>
                          <a href="#">Link 2</a>
                          <a href="#">Link 3</a>
                        </div>
                    </div>
</div>
</div>

<div class="dropdown">
      <button class="dropbtn">Home & Furniture
        <i class="fa fa-caret-down"></i>
      </button>
  <div class="dropdown-content">

                      <div class="row">
                        <div class="column">
                          <h3>Kitchen & Dining</h3>
                          <a href="#">Link 1</a>
                          <a href="#">Link 2</a>
                          <a href="#">Link 3</a>
                        </div>
                        <div class="column">
                          <h3>Furniture</h3>
                          <a href="#">Link 1</a>
                          <a href="#">Link 2</a>
                          <a href="#">Link 3</a>
                        </div>
                        <div class="column">
                          <h3>Furnishing</h3>
                          <a href="#">Link 1</a>
                          <a href="#">Link 2</a>
                          <a href="#">Link 3</a>
                        </div>
                    </div>
</div>
</div>

<div class="dropdown">
      <button class="dropbtn">Sports, Books & more
        <i class="fa fa-caret-down"></i>
      </button>
  <div class="dropdown-content">

                      <div class="row">
                        <div class="column">
                          <h3>Books</h3>
                          <a href="#">Link 1</a>
                          <a href="#">Link 2</a>
                          <a href="#">Link 3</a>
                        </div>
                        <div class="column">
                          <h3>Gaming & car Accessories</h3>
                          <a href="#">Link 1</a>
                          <a href="#">Link 2</a>
                          <a href="#">Link 3</a>
                        </div>
                        <div class="column">
                          <h3>Sports</h3>
                          <a href="#">Link 1</a>
                          <a href="#">Link 2</a>
                          <a href="#">Link 3</a>
                        </div>
                    </div>
</div>
</div>

<a href="#home">Offers</a>




















</div>











);

export default CategoryBar;
