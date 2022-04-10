import { 
    Card,
    Typography, 
    Grid
} from "@mui/material";
import React from "react";

const TopTweet = ({ tweet }) => {
    return <>
        <Typography variant="h5">{tweet.message}</Typography>
        <div style={{textAlign: "end"}}>
        <Typography variant="h6">By: @{tweet.user}</Typography>
        </div>
        

    </>
}

export default TopTweet;