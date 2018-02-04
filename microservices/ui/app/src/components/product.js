import React from 'react';
import Paper from 'material-ui/Paper';
import Qh from './Qh.png';
import QhBig from './QhBig.png';
import QhGreen from './QhGreen.png';
import QhgreenBig from './QhgreenBig.png';
import '../App.css';
import Button from 'material-ui/Button';
import Hidden from 'material-ui/Hidden/Hidden';


class Product extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      productImage1:'',
      productImage2:'',
      productImage3:'',
      productVariableImage:'',
      product: [],
     
    }
  }
  handleImage1 = (e) => {
    this.setState({productVariableImage:this.state.productImage1});
  }
  
  handleImage2 = (e) => {
    this.setState({productVariableImage:this.state.productImage2});
  }
  handleImage3 = (e) => {
    this.setState({productVariableImage:this.state.productImage3});
    }


  loadData() {
    fetch('https://app.banner20.hasura-app.io/product?product_id=' + this.props.match.params.productId)
      .then(response => response.json())
      .then(json => {
        this.setState({
          product: json,
        });
        this.state.product.map((p, i)=>this.setState({productVariableImage:p.product_image, 
                                                      productImage1:p.product_image_1,
                                                      productImage2:p.product_image_2,
                                                      productImage3:p.product_image_3}));
      });
  }
  componentDidMount() {
    this.loadData();
  }
  render() {
    return (
      <div>
        {
          this.state.product.map((p, i) =>
          
          //Primary Image Loading
        <div className="row">
          <div className="col l3">
            <div className="row">
              <div className="col s4">
                <Paper zDepth={1}  >
                  <div>
                    <img style={{maxWidth:50+'px', height:50+'px',overflow:Hidden}} onClick={this.handleImage1} src={p.product_image_1} alt={p.product_name} />
                  </div>
                </Paper>
              </div>
            </div>
            <div className="row">
              <div className="col s4">
                <Paper zDepth={1}  >
                  <div>
                    <img style={{maxWidth:50+'px', height:50+'px',overflow:Hidden}}  onClick={this.handleImage2} src={p.product_image_2} alt={p.product_name} />
                  </div>
                </Paper>
              </div>
            </div>
            <div className="row">
              <div className="col s4">
                <Paper zDepth={1}  >
                  <div>
                    <img style={{maxWidth:50+'px', height:50+'px',overflow:Hidden}}  onClick={this.handleImage3} src={p.product_image_3} alt={p.product_name} />
                  </div>
                </Paper>
              </div>
            </div>
          </div>
          <div className="col l5">
            <Paper >
              <div>
                <img style={{maxWidth:250+'px', height:450+'px',overflow:Hidden}} src={this.state.productVariableImage} />
              </div>
            </Paper>
          </div>

          <div className="col l4">
            <div>
              <Paper zDepth={0}>
                <div>
                  <div>
                    <p className="ProductdescriptionText">
                      {p.product_name}
                    </p>
                  </div>
                  <div>
                    <p>MRP:{p.price}</p>

                  </div>
                  <div className="row">
                    <div className="col s6">
                      <input placeholder="pincode" type="text" class="validate" />
                    </div>
                    <div className="col s6">
                      <Button raised >Check</Button>

                    </div>
                  </div>
                </div>



                <div className="row">
                  <div className="col s6">
                    <Button raised >Add To Cart</Button >
                  </div>
                  <div className="col s6">
                    <Button raised className="blackText">Buy Now</Button>

                  </div>
                </div>
                <div className="row">
                  <div className="col s12">
                    <Paper zDepth={0}>
                      <p className="ProductdescriptionText">Details</p>
                     <p>{p.product_description}</p>
                    </Paper>
                  </div>
                </div>
              </Paper>
            </div>
          </div>
        </div>
        )
        }        
      </div>
    )
  }
}
export default Product;