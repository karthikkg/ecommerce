import fetch from 'isomorphic-fetch';
import { projectConfig, getSavedToken} from './config';


const authenticateUser = (username, password, shouldSignUp) => {
    var path = shouldSignUp ? '/signup' : '/login';
    var requestOptions = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
          provider: "username",
          data: {
            "username": username,
            "password": password
          }
        })
    };
    console.log("entered authen");
    return fetch(projectConfig.url.auth + path, requestOptions)
    .then(function(response) {
      console.log("returned response")
      return response.json();
    })
    .catch(function(error) {
      console.log('Request Failed:' + error);
    });
  }

  const Userinfo = () => {
    var token = getSavedToken();
    console.log(token);
    var requestOptions = {
      "method": "GET",
      "headers": {
          "Content-Type": "application/json",
          "Authorization": "Bearer " + token
      }
  };
    console.log("entered info");
    return fetch(projectConfig.url.auth + "/user/info", requestOptions)
    .then(function(response) {
      console.log("returned response")
      return response.json();
    })
    .catch(function(error) {
      console.log('Request Failed:' + error);
    });
  }
  const MakeUser = (hasura_id,lastname,email,phonenumber,firstname) => {
    var requestOptions = {
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Authorization": "Bearer 9bda6d9c532211017a297151a08734ec43434f0e9e2709f8"
        }
    };
    var body = {
      "type": "insert",
      "args": {
          "table": "customer",
          "objects": [
              {
                "hasura_id": hasura_id,
                "lastname": lastname,
                "email": email,
                "phonenumber": phonenumber,
                "firstname": firstname
              }
          ]
      }
    };
    requestOptions["body"] = JSON.stringify(body);
    return fetch(projectConfig.url.data, requestOptions)
    .then(function(response) {
      return response.json();
    })
    .catch(function(error) {
      console.log('Request Failed:' + error);
    });
  };
  
  const Logout = () => {
    var token = getSavedToken();
    console.log(token);
    var requestOptions = {
      "method": "POST",
      "headers": {
          "Content-Type": "application/json",
          "Authorization": "Bearer " + token
      }
  };
    console.log("loggedout");
    return fetch(projectConfig.url.auth + "/user/logout", requestOptions)
    .then(function(response) {
      console.log("returned response")
      return response.json();
    })
    .catch(function(error) {
      console.log('Request Failed:' + error);
    });
  }
  export {
    authenticateUser,
    Userinfo,
    MakeUser
  }