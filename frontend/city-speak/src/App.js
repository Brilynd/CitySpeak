import React, { useState, useEffect } from "react";
import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";
import { Typography, Divider } from "@mui/material";
import "./App.css";
import { PieChart} from "./Chart";
import MyMap from "./Map";
import TopTweet from "./TopTweet";
import data from './data';



function App() {
  const [center, setCenter] = useState([0, 0]);
  const [location, setLocation] = useState("");
  const [stateData, setStateData] = useState({});

  const getUserLocation = () => {
    fetch(
      "https://geolocation-db.com/json/0215bdd0-b516-11ec-b0a9-fdbfeccd28cf"
    )
      .then((res) => res.json())
      .then((data) => {
        setCenter([data.latitude, data.longitude]);
        setLocation(data.state);
      });
  };

  const tweets = [];
  for (let index = 0; index < Object.keys(data.state).length; index++) {
    const tweet = {
      state: data.state[index],
      popular_category: data.popular_category[index],
      tweet: data.tweet[index],
      user: data.user[index],
      analytics: data.Analytics[index],
    }
    tweets.push(tweet)
  }

  useEffect(() => {
    getUserLocation();
  }, []);

  useEffect(() => {
    let dataPoint = tweets.filter((tweet) => tweet.state === location);
    if (dataPoint.length > 0) {
      dataPoint = dataPoint[0];
    }

    setStateData(dataPoint)
  }, [location])

  return (
    <div>
      <Grid container spacing={3} id="content">
        <Grid item xs={6}>
          <Typography variant="h3" className="title">
            State Speak
          </Typography>
        </Grid>
        <Grid item xs={6}>
          
        </Grid>


        

        <Grid item container spacing={3} style={{ height: "90vh" }}>
          <Grid item xs={6}>
            <MyMap
              center={center}
              onLocationChange={(newLocation, newCenter) => {
                setLocation(newLocation);
                setCenter(newCenter);
              }}
            />
          </Grid>
          <Grid item xs={6}>
            <Card className="right-side">
              <Typography variant="h3" style={{color: "#180849"}}>{location}</Typography>
              <Divider style={{ marginTop: "10px", marginBottom: "10px" }} />
              
              {stateData.length == 0 ?
                <>
                  <Typography variant="h4" fontSize="50px" textAlign='center' marginTop="25%" letterSpacing=".5px">
                    No data found for this state!
                  </Typography>
                </>
              :
              <>
                <Typography variant="h4" fontSize="32px" textAlign='center' marginBottom="15px" letterSpacing=".5px">Top Tweet</Typography>
                <TopTweet tweet={stateData} />

                <Typography variant="h4" fontSize="32px" textAlign='center' marginBottom="15px" letterSpacing=".5px">State Tweet Categories</Typography>
                <div className="chart-container">
                  <PieChart data={stateData}/>
                </div>
              </>
              }
              

            </Card>
          </Grid>
        </Grid>
      </Grid>
    </div>
  );
}

export default App;
