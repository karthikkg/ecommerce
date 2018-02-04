import React from 'react';
import Paper from 'material-ui/Paper';
import Qh from './Qh.png';
import QhBig from './QhBig.png';
import QhGreen from './QhGreen.png';
import QhgreenBig from './QhgreenBig.png';
import '../App.css';
import Button from 'material-ui/Button';


class Product extends React.Component {
  constructor(props) {
    super(props);
    console.log();
    this.state = {
      product: []
    }
  }


  loadData() {
    fetch('https://app.banner20.hasura-app.io/product?product_id=' + this.props.match.params.productId)
      .then(response => response.json())
      .then(json => {
        this.setState({
          product: json,
        });
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
        <div className="row">
          <div className="col l3">
            <div className="row">
              <div className="col s4">
                <Paper zDepth={1}  >
                  <div>
                    <img src={p.product_image_1} alt={p.product_name} />
                  </div>
                </Paper>
              </div>
              <div className="col s4">
                <Paper zDepth={1}  >
                  <div >
                    <img src={p.product_image_1} alt={p.product_name} />
                  </div>
                </Paper>
              </div>
            </div>
            <div className="row">
              <div className="col s4">
                <Paper zDepth={1}  >
                  <div >
                    <img src={p.product_image_2} alt={p.product_name} />
                  </div>
                </Paper>
              </div>
              <div className="col s4">
                <Paper zDepth={1}  >
                  <div >
                    <img src={p.product_image_3} alt={p.product_name} />
                  </div>
                </Paper>
              </div>
            </div>
            <div className="row">
              <div className="col s4">
                <Paper zDepth={1}  >
                  <div >
                    <img src={p.product_image} alt={p.product_name} />
                  </div>
                </Paper>
              </div>
              <div className="col s4">
                <Paper zDepth={1}  >
                  <div >
                    <img src={p.product_image_1} alt={p.product_name} />
                  </div>
                </Paper>
              </div>
            </div>
          </div>
          <div className="col l5">
            <Paper >
              <div>
                <img src={p.product_image} />
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
                      <Button raised label="Check"/>

                    </div>
                  </div>
                </div>



                <div className="row">
                  <div className="col s6">
                    <Button raised label="Add to cart"/>
                  </div>
                  <div className="col s6">
                    <Button raised label="Buy Now" />

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