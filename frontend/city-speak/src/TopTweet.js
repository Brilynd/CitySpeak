import { 
    Card,
    Typography, 
    Grid
} from "@mui/material";
import React from "react";

const TopTweet = ({ tweet }) => {
    return <>
        <Typography className="tweet" variant="h5">&#8220;{tweet.tweet}&#8221;</Typography>
        <div style={{textAlign: "left", marginBottom: '10px'}}>
        <Typography variant="h6" fontSize="12px" letterSpacing="1px" color="rgb(63, 63, 63)">By: @{tweet.user}</Typography>
        </div>
        

    </>
}

export default TopTweet;