import React from 'react';
import {connect} from 'react-redux';
import {StyleSheet, View, KeyboardAvoidingView, ScrollView} from 'react-native';
import {Text, H1, Container, Content, Button, Card, CardItem, Body, Form, Item, Label, Input, Icon, Picker} from 'native-base';

class Login extends React.Component {
    constructor(){
        super();
        this.state={
            showLogin:true,
            userStatus:'seller'
        };
        }

    handleSignup=() => {
        this.setState({
          showLogin:false
        });
    }

    setShowLogin=() => {
      this.setState({
        showLogin:true
      });
    }

    changeStatus=(value) => {
      this.setState({
        userStatus:value
      });
    }
  
  render() {
    return (
      <KeyboardAvoidingView behavior='padding'>
        <ScrollView contentContainerStyle={styles.container}>
            <Form style={styles.form}>
            {(this.state.showLogin)?
              <View style={{height:30}}/>:
              <Button transparent dark iconLeft onPress={this.setShowLogin}><Icon name='arrow-back'/></Button>
            }
              <H1 style={{color:'rgba(0,0,0,0.87)'}}>Welcome!</H1>
              <Item floatingLabel style={{width:'70%'}}>
                <Label>E-mail</Label>
                <Input style={{color:'black'}}/>
              </Item>
              <Item floatingLabel style={{width:'70%'}}>
                <Label>Password</Label>
                <Input secureTextEntry={true} style={{color:'black'}}/>
              </Item>
              {(this.state.showLogin)?null:
              <View>
                <Item floatingLabel style={{width:'70%'}}>
                  <Label>Confirm password</Label>
                  <Input secureTextEntry={true} style={{color:'black'}}/>
                </Item>
                <Item floatingLabel style={{width:'70%'}}>
                  <Label>Full Name</Label>
                  <Input style={{color:'black'}}/>
                </Item>
                <Item floatingLabel style={{width:'70%'}}>
                  <Label>Mobile number</Label>
                  <Input keyboardType='numeric' style={{color:'black'}}/>
                </Item>
                <Picker style={{marginLeft:5}} selectedValue={this.state.userStatus} onValueChange={this.changeStatus}>
                  <Picker.Item label='Buyer' value='buyer'/>
                  <Picker.Item label='Seller' value='seller'/>
                </Picker>
              </View>
              }
              <View style={{height:20}}/>
              {(this.state.showLogin)?
                <Button full success style={{marginLeft:15, marginRight:15}} onPress={this.props.update}><Text>Log In</Text></Button>
              :null}
              <View style={{height:10}}/>
              <Button full primary style={{marginLeft:15, marginRight:15}} onPress={this.handleSignup}><Text>Sign Up</Text></Button>
            </Form>
        </ScrollView>
      </KeyboardAvoidingView>
    );
  }
}

const styles=StyleSheet.create({
  container:{
    height:'100%',
    backgroundColor:'rgb(230,230,230)', 
    paddingLeft:10, 
    paddingRight:10, 
    paddingTop:20,
    paddingBottom:20,  
    justifyContent:'center'
  },
  form:{
    backgroundColor:'rgba(255,255,255,0.87)', 
    alignItems:'center',
    borderRadius:10

  }
});

export default connect(
    (store) => {
        return store;
    }
)(Login);