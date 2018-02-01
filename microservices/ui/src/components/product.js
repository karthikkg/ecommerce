import React from 'react';
import Paper from 'material-ui/Paper';
import Qh from './Qh.png';
import QhBig from './QhBig.png';
import QhGreen from './QhGreen.png';
import QhgreenBig from './QhgreenBig.png';
import '../App.css';
import Button from 'material-ui/Button';


class Product extends React.Component{
  render(){
    return (
      <div>
      <div className="row">
          <div className="col l3">
               <div className="row">
                     <div className="col s4">
                       <Paper   zDepth={1}  >
                          <div>
                            <img src={Qh} alt="quickheal" />
                          </div> 
                       </Paper>
                     </div>

                     <div className="col s4">
                       <Paper   zDepth={1}  >
                          <div >
                                <img src={Qh} alt="quickheal" />
                          </div> 
                       </Paper>
                    </div>
               </div>

               <div className="row">
                   <div className="col s4">
                     <Paper   zDepth={1}  >
                        <div >
                              <img src={Qh} alt="quickheal" /> 

                        </div> 
                     </Paper>
                   </div>
                   <div className="col s4">
                     <Paper   zDepth={1}  >
                        <div >
                        <img src={Qh} alt="quickheal" /> 
                        </div> 
                    </Paper>
                  </div>
               </div>
               <div className="row">
                   <div className="col s4">
                     <Paper   zDepth={1}  >
                        <div >
                        <img src={Qh} alt="quickheal" /> 
                        </div> 
                    </Paper>
                  </div>
                   <div className="col s4">
                     <Paper   zDepth={1}  >
                        <div >
                         <img src={Qh} alt="quickheal" /> 
                        </div> 
                     </Paper>
                   </div>
               </div>
       </div>
<div className="col l5">
             <Paper >
                    <div>
                         <h3 marginLeft='1em'>Quickheal Antivirus</h3>
                         <img src={QhBig}  />
                    </div>
             </Paper>
 </div>

 <div className="col l4">
                 <div>
                   <Paper zDepth={0}>
                     <div>
                            <div>
                                   <p className="ProductdescriptionText">Quick Heal Antivirus Pro Latest Version - 2 PCs, 1 Year (DVD)</p>                                   

                            </div>  
                             <div>
                               <p>MRP:1000rs</p>

                             </div>
                                 <div className="row">
                                   <div className="col s6">
                                        <input placeholder="pincode"  type="text" class="validate"/>
                                   </div>
                                   <div className="col s6">
                                           <Button raised label="Check" primary={true}  />

                                   </div>
                                 </div>
                                         

                      </div>
                       
                              

                     <div className="row">
                       <div className="col s6">
                               <Button raised label="Add to cart" primary={true}  />
                       </div>
                       <div className="col s6">
                               <Button raised label="Buy Now" primary={true}  />

                       </div>
                     </div>
                   <div className="row">
                       <div className="col s12">
                            <Paper zDepth={0}>
                              <p className="ProductdescriptionText">Details</p>
                               <ol>
                                  <li>Upgradation of the product (if needed) can be done from- quickheal.co.in </li>
                                  <li>upgrade Protects your data from data-stealing malware, wipers </li>
                                  <li>Stops unknown threats that traditional antivirus software do not </li>
                                  <li>Automatically blocks websites that can infect your PC</li>
                                  <li>Ransomware protection, malware protection, web security, anti key-logger, safe-mode protection, wiper protection</li>
                               </ol>
                            </Paper>
                        </div>
                    </div>
                   </Paper>
                 </div>
     </div> 
</div>
</div>

      
    );
  }
}
export default Product;