import { 
    Card,
    Typography, 
} from "@mui/material";

const TopTweet = ({ tweet }) => {
    return <Card className="tweet">
        <Typography variant="h3">{tweet.user}</Typography>
        <Typography variant="h4">{tweet.message}</Typography>
        <Typography variant="h5">{tweet.location}</Typography>
    </Card>
}

export default TopTweet;