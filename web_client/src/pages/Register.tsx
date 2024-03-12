import { useState, useEffect } from 'react'
import { Link, useNavigate } from 'react-router-dom'

import { Container, Paper, Typography, TextField, Button } from '@mui/material'

function Register() {
  const navigate = useNavigate();
  
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleRegistration = (e: any) => {
    e.preventDefault();
    if ((username == "") && (password == "")) {
      return;
    } else {
      console.log(username)
    }
  }

  return (
    <Container component="main" maxWidth="xs" sx={{ marginTop: 20, marginBottom: 20 }}>
      <Paper elevation={2} sx={{ padding: 5 }} >
        <Typography component="h1" variant="h5" align='center'>
          REGISTER
        </Typography>
        <form onSubmit={handleRegistration}>
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="username"
            label="Username"
            name="username"
            autoFocus
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            size="large"
          >
            Register
          </Button>
        </form>
      </Paper>
    </Container>
  )
}

export default Register
