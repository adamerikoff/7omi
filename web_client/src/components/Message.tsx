import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';

interface Props {
    author: string;
    text: string;
}

function Message({ text, author }: Props) {
    const isMine = author === "admin";

    return (
        <div style={{ textAlign: isMine ? 'right' : 'left', marginBottom: 8 }}>
        <Paper elevation={3} style={{ padding: 12, background: isMine ? '#f0f0f0' : '#e0e0e0' }}>
            <Typography variant="h6">{author}</Typography>
            <Typography variant="body1">{text}</Typography>
        </Paper>
        </div>
    );
}

export default Message;