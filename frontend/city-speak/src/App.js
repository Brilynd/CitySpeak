import React, { useState, useEffect } from 'react';
import Grid from '@mui/material/Grid';
import "App.css"
import MyMap from './Map';


function App() {
  const [center, setCenter] = useState([48.85837009999999, 2.2944813]);
  const [location, setLocation] = useState("");

  const getUserLocation = () => {
    fetch("https://geolocation-db.com/json/0215bdd0-b516-11ec-b0a9-fdbfeccd28cf")
    .then(res => res.json())
    .then(data => {
      console.log(data)
      setCenter([data.latitude, data.longitude]);
      setLocation(data.city);
    })
  }

  useEffect(() => {
    getUserLocation();
  },[]);
  return (
    <div>
      <header>
        <h1>City-Speak</h1>
      </header>
      <Grid container style={{minHeight: "80vh"}}>
        <Grid item xs={6}>
          <MyMap center={center}/>
        </Grid>
        <Grid item xs={6}>
          <h2>Current Location: {location}</h2>
        </Grid>
      </Grid>
      
    </div>
  );
}

export default App;
