import React, { useState, useEffect } from 'react';
import Grid from '@mui/material/Grid';
import Card from '@mui/material/Card';
import { Typography } from '@mui/material';
import "./App.css"
import {PieChart,data} from './Chart';
import MyMap from './Map';
import TopTweet from './TopTweet';

function App() {
  const [center, setCenter] = useState([0, 0]);
  const [location, setLocation] = useState("");

  const getUserLocation = () => {
    fetch("https://geolocation-db.com/json/0215bdd0-b516-11ec-b0a9-fdbfeccd28cf")
    .then(res => res.json())
    .then(data => {
      setCenter([data.latitude, data.longitude]);
      setLocation(data.state);
    })
  }

  useEffect(() => {
    getUserLocation();
  },[]);

  const tweet = {
    user: "John-Smith",
    message: "This is some random tweet",
    location: location
  }

  return (
    <div>
        <Grid container spacing={3} id="content">
          <Grid item xs={6}>
            <Typography variant="h3">City-Speak</Typography>
          </Grid>
       
          <Grid item container spacing={3} style={{height: "90vh"}}>
          <Grid item xs={6}>
            <MyMap center={center} onLocationChange={(newLocation, newCenter) => {
              setLocation(newLocation);
              setCenter(newCenter);
            }}/>
          </Grid>
          <Grid item xs={6}>
            <Card className="right-side">
              <Typography variant="h4">Current State: {location}</Typography>
              <TopTweet tweet={tweet}/>
              <PieChart   width={100}
  height={50}
  options={{ maintainAspectRatio: false }}/>
            </Card>
           
          </Grid>

          </Grid>
      </Grid>
      
    </div>
  );
}

export default App;
