import { 
    Card,
    Typography, 
    Grid
} from "@mui/material";
import React from "react";

const TopTweet = ({ tweet }) => {
    return <>

        <Grid container>
            <Grid item xs={8}>
                <Typography variant="h5">{tweet.user}</Typography>
            </Grid>
            <Grid item xs={4}>
                <Typography variant="h6"><i>Location: {tweet.location}</i></Typography>
            </Grid>
        </Grid>

        <Typography variant="h5">{tweet.message}</Typography>

    </>
}

export default TopTweet;