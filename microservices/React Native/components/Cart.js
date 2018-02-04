import React, { Component } from 'react';
import {StatusBar, Platform, View, StyleSheet, TouchableOpacity} from 'react-native';
import {Text, Icon} from 'native-base';
import Item from './Item';
import BasketContainer from './BasketComponent';
import Footer from './Footer';

export default class Cart extends Component {
  render() {
    return (
      <View style={{ flex: 1 }}>
        <View style={styles.containerStyle}>
        	<Item/>
      	</View>
        <BasketContainer/>
        <Footer/>
      </View>
      
    );
  }
}

const styles = StyleSheet.create({
  containerStyle: {
    flex: 4,
    backgroundColor: '#DCDCDC'
  }
});

