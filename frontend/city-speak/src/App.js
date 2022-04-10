import React, { useState, useEffect } from 'react';
import Grid from '@mui/material/Grid';
import Card from '@mui/material/Card';

import "./App.css"
import MyMap from './Map';

import { styled, alpha } from '@mui/material/styles';
import SearchIcon from '@mui/icons-material/Search';


function App() {
  const [center, setCenter] = useState([48.85837009999999, 2.2944813]);
  const [location, setLocation] = useState("");

  const getUserLocation = () => {
    fetch("https://geolocation-db.com/json/0215bdd0-b516-11ec-b0a9-fdbfeccd28cf")
    .then(res => res.json())
    .then(data => {
      setCenter([data.latitude, data.longitude]);
      setLocation();
    })
  }

  useEffect(() => {
    getUserLocation();
  },[]);
  return (
    <div>
      <header>
        <Grid container>
          <Grid item xs={6}>
            <h1>City-Speak</h1>
          </Grid>
          <Grid item xs={6}>
            <div id="search-container">
              <SearchIcon />
              <input type="text" placeholder="Search" onChange={(e) => setLocation(e.target.value)} />
            </div>
          </Grid>
        </Grid>
        
      </header>
      <Grid container style={{minHeight: "80vh"}}>
        <Grid item xs={6}>
          <MyMap center={center}/>
        </Grid>
        <Grid item xs={6} className="right-side">
          <Card className="card">
            <h2>Current Location: {location}</h2>
            <ul>
              <li>Item 1</li>
              <li>Item 2</li>
              <li>Item 3</li>
            </ul>
          </Card>
          
        </Grid>
      </Grid>
      
    </div>
  );
}

export default App;
