import React, { useState, useEffect } from 'react';
import Grid from '@mui/material/Grid';
import Card from '@mui/material/Card';
import { Typography } from '@mui/material';
import Autocomplete from "react-google-autocomplete";
import "./App.css"
import MyMap from './Map';
import Address from './SearchLocationInput';
import SearchIcon from '@mui/icons-material/Search';
import parseAddress from "parse-address"

function App() {
  const [center, setCenter] = useState([48.85837009999999, 2.2944813]);
  const [location, setLocation] = useState("");
  const [returnLocation,setReturnLocation] = useState(" ")

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

  useEffect(()=>{
    spliceLocation(returnLocation)
  },[returnLocation])

  const spliceLocation=(location)=>{
 
    
  }


  
  return (
    <div>
        <Grid container spacing={3} id="content">
          <Grid item xs={6}>
            <Typography variant="h3">City-Speak</Typography>
          </Grid>
          <Grid item xs={6} className="right-side">
            <div id="search-container">
            {/* <Address returnLocation={(returnLocation)=>setReturnLocation(returnLocation)}/> */}
            <select name="" id="">
              <option value="">AL</option>
              <option value="">AK</option>
              <option value="">AZ	</option>
              <option value="">AR</option>
              <option value="">CA</option>
              <option value="">CO</option>
              <option value="">CT</option>
              <option value="">DE</option>
              <option value="">DC</option>
              <option value="">FL</option>
              <option value="">GA</option>
              <option value="">HI</option>
              <option value="">ID</option>
              <option value="">IL</option>
              <option value="">IN</option>
              <option value="">IA</option>
              <option value="">KS</option>
              <option value="">KY</option>
              <option value="">LA</option>
              <option value="">ME</option>
              <option value="">MD</option>
              <option value="">MA	</option>
              <option value=""></option>
            </select>
            </div>
          </Grid>
       
          <Grid item container spacing={3} style={{height: "90vh"}}>
          <Grid item xs={6}>
            <MyMap center={center} onLocationChange={(newLocation, newCenter) => {
              setLocation(newLocation);
              setCenter(newCenter);
            }}/>
          </Grid>
          <Grid item xs={6}>
            <Card className="card">
              <Typography variant="h4">Current State: {location}</Typography>
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
