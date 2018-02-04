import React, { Component } from 'react';
import GridList, { GridListTile } from 'material-ui/GridList';
import Slider from 'react-slick';
import { Link } from 'react-router-dom';
export default class ImageSlider extends Component {
  render() {
    var settings = {
      dots: true,
      arrows: true,
      infinite: true,
      speed: 1000,
      autoplay: true,
      slidesToShow: 1,
      slidesToScroll: 1,
      centerMode: true,
    };

    return (
      <Slider {...settings} className="imageSlider">
        {
          this.props.products.map((product, i) =>
            <div>
              <Link to={'/product/' + product.id}>
                <GridList cols={2}/** cellHeight={400} affects the height**/>
                  <GridListTile cols={1} >
                    <img src={product.first_image_url} alt={product.name} />
                  </GridListTile>
                  <GridListTile cols={1}>
                    <h6>{product.name}</h6><h6>{product.price}</h6>
                  </GridListTile>
                </GridList>
              </Link>
            </div>
          )
        }
      </Slider>
    );
  }
}