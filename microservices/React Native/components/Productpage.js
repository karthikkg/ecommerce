import React from 'react';
import {View, Image, ScrollView, TextInput, StyleSheet } from 'react-native';
import {H1, H2, Text, Item,Label,Input, Button}  from 'native-base';
 
export default class Productpage extends React.Component{
    constructor(props){
        super(props);
        this.state={
            image:'',
            name:'Loading...',
            desc:'',
            price:''
        };
    }

    componentWillMount(){
        fetch('https://app.banner20.hasura-app.io/product?product_id='+this.props.navigation.state.params.product_id).then((res) => {
            return res.text();
        }).then((data) => {
            data=JSON.parse(data)[0];
            this.setState({
                image:data.product_image,
                name:data.product_name,
                desc:data.product_description,
                price:data.price.toString()
            });
        });
    }

    render() {
        return(
            <ScrollView contentContainerStyle={styles.main}>

                <Image style={styles.image} source={{uri:this.state.image}}/> 
                <H1>{this.state.name}</H1>
                <H2 style={{color:'rgba(0,0,0,0.7)'}}>{this.state.price}₹</H2>
                
                <View style={styles.view}>
                    <Button style={{backgroundColor:'#1A237E'}} onPress={() => {}}>
                            <Text>Add to cart</Text>
                    </Button>
                    <Button style={{backgroundColor:'#1A237E'}} onPress={() => {}}>
                            <Text>Buy Now</Text>
                    </Button>
                </View>

                <Text style={styles.text1}>
                    Product Details
                </Text>
                <Text  style={styles.text2}>
                    {this.state.desc}
                </Text>

            </ScrollView>
                
        );
    }
}

 const styles = StyleSheet.create({
  view: {
   flexDirection:'row',
   padding:10   ,
   justifyContent: 'space-between'
  },
  image:{
      width:'90%',
      height:300,
      resizeMode:'contain'
  },
  main:{
      padding:10
  },
  input:
  {
    height:17,
    width:180,
    fontSize:16,
    marginVertical:10,
  },
  heading:
  {
    fontSize:18,
    color:'#1A237E',
    fontWeight:'bold'
  },
  text1:
  {
    fontSize:16,
    color:'#1A237E',
    fontWeight:'500',
    padding:10
  },
  text2:
  {
    fontSize:16,
    color:'#1A237E',
    fontWeight:'200'
  },

});