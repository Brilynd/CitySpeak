import { 
    Card,
    Typography, 
    Grid
} from "@mui/material";
import React from "react";

const TopTweet = ({ tweet }) => {
    return <>
        <Typography variant="h5">{tweet.tweet}</Typography>
        <div style={{textAlign: "end"}}>
        <Typography variant="h6">By: @{tweet.user}</Typography>
        <Typography variant="h6">Category: {tweet.popular_category}</Typography>
        </div>
        

    </>
}

export default TopTweet;