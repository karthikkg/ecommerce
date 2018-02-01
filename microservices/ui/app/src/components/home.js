import React,{Component} from 'react';
import TitlebarGridList from './productGrid'
import ImageSlider from './imageSlider';
export default class Home extends Component{
    constructor(){
        super();
        this.state={
            products:
            [
                {
                  "first_image_url": "https://filestore.banner20.hasura-app.io/v1/file/2367e969-0ac1-43c2-9ff5-0c0ed1d2031e", 
                  "id": 10, 
                  "name": "Google Pixel 2 (Just Black, 64 GB)\u00a0\u00a0(4 GB RAM)", 
                  "price": 49999, 
                  "product_url": "https://app.banner20.hasura-app.io/product?product_id=10"
                }, 
                {
                  "first_image_url": "https://filestore.banner20.hasura-app.io/v1/file/d0dc66ca-ab47-48ec-ab3f-23916a4deff1", 
                  "id": 11, 
                  "name": "Apple MacBook Pro Core i5 7th Gen - (8 GB/256 GB SSD/Mac OS Sierra) MPXV2HN/A\u00a0\u00a0(13.3 inch, SPace Grey, 1.37 kg)", 
                  "price": 139999, 
                  "product_url": "https://app.banner20.hasura-app.io/product?product_id=11"
                }, 
                {
                  "first_image_url": "https://filestore.banner20.hasura-app.io/v1/file/0d4ccf3b-bd0f-46ce-bd81-b2822c5a5608", 
                  "id": 12, 
                  "name": "Immortals of Meluha\u00a0\u00a0(English, Paperback, Amish)", 
                  "price": 195, 
                  "product_url": "https://app.banner20.hasura-app.io/product?product_id=12"
                }, 
                {
                  "first_image_url": "https://filestore.banner20.hasura-app.io/v1/file/14ab2e67-e364-43f0-9a95-60c7ab64e35e", 
                  "id": 13, 
                  "name": "Scion of Ikshvaku\u00a0\u00a0(English, Paperback, Amish)", 
                  "price": 170, 
                  "product_url": "https://app.banner20.hasura-app.io/product?product_id=13"
                }, 
                {
                  "first_image_url": "https://filestore.banner20.hasura-app.io/v1/file/93edcfa0-c08f-4c95-9436-ee3609522084", 
                  "id": 14, 
                  "name": "Samsung Series 6 123cm (49 inch) Full HD Curved LED Smart TV\u00a0\u00a0(49M6300)", 
                  "price": 59999, 
                  "product_url": "https://app.banner20.hasura-app.io/product?product_id=14"
                }, 
                {
                  "first_image_url": "https://filestore.banner20.hasura-app.io/v1/file/f578000a-8ea1-423b-80eb-e24f393939ea", 
                  "id": 15, 
                  "name": "Magnus Chase and the Hammer of Thor\u00a0\u00a0(English, Paperback, Rick Riordan)", 
                  "price": 360, 
                  "product_url": "https://app.banner20.hasura-app.io/product?product_id=15"
                }, 
                {
                  "first_image_url": "https://filestore.banner20.hasura-app.io/v1/file/852c6c6b-10b4-4741-ad03-0816071daa5a", 
                  "id": 16, 
                  "name": "Percy Jackson and the Greek Heroes\u00a0\u00a0(English, Paperback, Rick Riordan)", 
                  "price": 403, 
                  "product_url": "https://app.banner20.hasura-app.io/product?product_id=16"
                }, 
                {
                  "first_image_url": "https://filestore.banner20.hasura-app.io/v1/file/d9753055-e621-4c5e-aeb5-c03c72fddd6f", 
                  "id": 17, 
                  "name": "Immortals of Meluha\u00a0\u00a0(English, Paperback, Amish)", 
                  "price": 195, 
                  "product_url": "https://app.banner20.hasura-app.io/product?product_id=17"
                }
              ]
        }
    }
    render(){
        return (
            <div>
              <div>
                {//{
                 // this.state.products.map((productData,i)=>
                 //   <div>
                 //           <h5>{productData.name}</h5>
                 //       </div>
                 //   )
                 //}
                }
                <ImageSlider products={this.state.products}/>
              </div>
              <br/>
              <TitlebarGridList  products={this.state.products}/>
            </div>         
 
        )
    }
} 