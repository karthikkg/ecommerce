import React, { Component } from 'react';
import cyan500 from 'material-ui/styles/colors';

import SearchBar from 'material-ui-search-bar';
import AutoComplete from 'material-ui/AutoComplete';

// ...

class Searchbar extends Component {
render() {
  return(
    <SearchBar
      onChange={() => console.log('onChange')}
      onRequestSearch={() => console.log('onRequestSearch')}
        hintText={"Search for Products Brand and more" }
      style={{
        position:'relative',
        float:'right',
        dispaly:'inline-block',
        marginLeft:'1em',
        
        maxWidth: '500px',
        maxHeight:35,
        width:'450px',
        backgroundColor:'white',
          border: '1px solid #00BCD4',
          

      }}
     
    />
     


  )
}
}
export default Searchbar;
