import { useState } from 'react';
import { TextField, Grid, Button } from '@mui/material';

function MessageTextField() {
  const [message, setMessage] = useState('');

  const handleChange = (event: any) => {
    setMessage(event.target.value);
  };

  const handleClick = () => {
    console.log(message)
  };

  return (
    <Grid container spacing={0} alignItems="center">
      <Grid item xs={9}>
        <TextField
          fullWidth
          variant="outlined"
          value={message}
          onChange={handleChange}
          placeholder="Type your message..."
        />
      </Grid>
      <Grid item xs={3}>
        <Button variant="contained" color="primary" onClick={handleClick} fullWidth size='large'>
          Send
        </Button>
      </Grid>
    </Grid>
  );
}

export default MessageTextField;
