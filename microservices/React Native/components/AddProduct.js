import React from 'react';
import {connect} from 'react-redux';
import {StyleSheet, View, TouchableOpacity, ScrollView} from 'react-native';
import {Text, Icon, List, ListItem, Thumbnail, Left, Right, Body, Button, Item, Input} from 'native-base';
import Store from './Store';



class AddProduct extends React.Component {
    render() {
        return(
            <ScrollView contentContainerStyle={{paddingTop:20}}>
                <List>
                    <ListItem>
                        <TouchableOpacity>
                            <Left>
                                <Thumbnail square size={80} source={{uri:'http://icons.iconarchive.com/icons/graphicloads/colorful-long-shadow/128/Add-icon.png'}}/>
                                <Text>Add Image</Text>
                            </Left>
                            <Body/>
                            <Right/>
                        </TouchableOpacity>
                    </ListItem>
                    <ListItem style={{borderBottomColor:'rgba(0,0,0,0.0)'}}>
                        <Item regular>
                            <Input placeholder='Enter Product Name'/>
                        </Item>
                    </ListItem>
                    <ListItem style={{borderBottomColor:'rgba(0,0,0,0.0)'}}>
                        <Item regular>
                            <Input multiline={true} numberOfLines={5} placeholder='Enter Product Description'/>
                        </Item>
                    </ListItem>
                    <ListItem style={{borderBottomColor:'rgba(0,0,0,0.0)'}}>
                        <Item regular>
                            <Input keyboardType='numeric' placeholder='Enter Price'/>
                        </Item>
                    </ListItem>
                </List>
                <View style={styles.button}>
                <Button><Text>Submit Product</Text></Button>
                </View>
            </ScrollView>
        );
    }
}

const styles = StyleSheet.create({
    button:{
        flexDirection:'row',
        justifyContent:'center',
        marginTop:50
    }
});

export default connect(
    (store) => {
        return store;
    }
)(AddProduct);
