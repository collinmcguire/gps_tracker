// Import modules
// #region
import 'bootstrap/dist/css/bootstrap.min.css';
import $ from 'jquery';
import Popper from 'popper.js';
import React from 'react';
import ReactDOM from 'react-dom/client';
//#endregion

// Import components 
// #region
import './css/App.css';
import Header from './components/header';
//#endregion

const App = () => (
  <React.Fragment>
    <Header />

    <main className='my-5 py-5'>
      <container className='px-0' class='text-center'>
        <h1>Welcome to the GPS Tracker App</h1>
      </container>
    </main>
  </React.Fragment>

);

export default App;
