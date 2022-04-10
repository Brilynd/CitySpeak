import { 
    Card,
    Typography, 
    Grid
} from "@mui/material";
import React from "react";

const TopTweet = ({ tweet }) => {
    return <>
        <Typography variant="h5" fontSize="24px" letterSpacing=".75px" marginBottom="15px">{tweet.tweet}</Typography>
        <div style={{textAlign: "left"}}>
        <Typography variant="h6" fontSize="12px" letterSpacing="1px" color="rgb(63, 63, 63)">By: @{tweet.user}</Typography>
        </div>
        

    </>
}

export default TopTweet;