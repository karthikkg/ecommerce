import React from 'react';
import GridList, { GridListTile, GridListTileBar } from 'material-ui/GridList';
import Subheader from 'material-ui/List/ListSubheader';
import IconButton from 'material-ui/IconButton';
import InfoIcon from 'material-ui-icons/Info';
import {Link } from 'react-router-dom';
/**
 * 
const tileData=[
    {
        img: imad,
        title: 'ProductName',
        author:'ABC',
        featured:true,
    },
    {
        img: imad,
        title: 'ProductName',
        author:'ABC',
        featured:true,
    },
    {
      img: imad,
      title: 'ProductName',
      author:'ABC',
      featured:true,
      },
      {
        img: imad,
        title: 'ProductName',
        author:'ABC',
        featured:true,
    }
]
 
 */
const styles = theme => ({
  root: {
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'space-around',
    overflow: 'hidden',
    backgroundColor: theme.palette.background.paper,
  },
  gridList: {
    width: 900,
    height: 200,
  },
  icon: {
    color: 'rgba(255, 255, 255, 0.54)',
  },
});

/**
 * The example data is structured as follows:
 *
 * import image from 'path/to/image.jpg';
 * [etc...]
 *
 * const tileData = [
 *   {
 *     img: image,
 *     title: 'Image',
 *     author: 'author',
 *   },
 *   {
 *     [etc...]
 *   },
 * ];
 */
class TitlebarGridList extends React.Component {
    render(){
      return(
        <div className="productGridRoot">
      <GridList cellHeight={180} className="productGridContaner">
        <GridListTile key="Subheader" cols={2} style={{ height: 'auto' }}>
          <Subheader component="div"> Products </Subheader>
        </GridListTile>
        {this.props.products.map(product => (
              <GridListTile key={product.id} className="productViewContainer">
                <img src={product.first_image_url} alt={product.name} />
                <Link to={'/product/'+product.id}>
                <GridListTileBar
                 
                  title={product.name}
                  subtitle={<span>At: {product.price}</span>}
                  actionIcon={
                    <IconButton className="productGridIcon">
                      <InfoIcon />
                    </IconButton>
                  }
                  />
                </Link>
              </GridListTile>
          
        ))}
      </GridList>
    </div>
      );
    }
}
export default TitlebarGridList;