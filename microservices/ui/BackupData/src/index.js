import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
//import SuperComponent1 from './components/SuperComponent1';
//import SuperComponent2  from './components/SuperComponent2';

import registerServiceWorker from './registerServiceWorker';
import '../node_modules/font-awesome/css/font-awesome.min.css';
import {BrowserRouter,Route,Switch} from 'react-router-dom';

ReactDOM.render(<App />, document.getElementById('root'));



/*  ReactDOM.render(
    <BrowserRouter>
        <div>
            <Switch>
                <Route path="/SuperComponent2" component={SuperComponent2}/>
                <Route path="/" component={App}/>
            </Switch>
        </div>
    </BrowserRouter>
    , document.querySelector('#root'));


    */

registerServiceWorker();
