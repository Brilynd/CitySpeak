import React, { useState, useEffect } from 'react';
import Grid from '@mui/material/Grid';
import Card from '@mui/material/Card';
import { Typography } from '@mui/material';

import "./App.css"
import MyMap from './Map';

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
        <Grid container spacing={3} id="content">
          <Grid item xs={6}>
            <Typography variant="h3">City-Speak</Typography>
          </Grid>
          <Grid item xs={6} className="right-side">
            <div id="search-container">
              <SearchIcon fontSize='large'/>
              <input type="text" placeholder="Search" onChange={(e) => setLocation(e.target.value)} />
            </div>
          </Grid>
       
          <Grid item container spacing={3} style={{height: "90vh"}}>
          <Grid item xs={6}>
            <MyMap center={center}/>
          </Grid>
          <Grid item xs={6}>
            <Card className="card">
              <Typography variant="h4">Current Location: {location}</Typography>
              <ul>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
              </ul>
            </Card>
          </Grid>
          </Grid>
      </Grid>
      
    </div>
  );
}

export default App;
