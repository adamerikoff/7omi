import { useState, useEffect } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { Container, Typography, TextField, Button, Paper } from '@mui/material';

import { setToken } from '../services/Auth';
import axios from "axios";

function Login() {
  const navigate = useNavigate();
  
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const login = (e: any) => {
    e.preventDefault();
    if ((username == "") && (password == "")) {
      return;
    } else {
      const url = "http://localhost:8000/auth/login"

      const form_data = new FormData()

      form_data.append("username", username)
      form_data.append("password", password)

      axios.post(url, form_data)
        .then(response => {
          const { access_token, username, token_type } = response.data; 
          console.log(response.data)
          if(access_token){
            console.log(access_token)
            console.log(username)
            console.log(token_type)
            setToken(access_token);
            navigate("/chat");
          }
        })
        .catch(function (error) {
          console.log(error, "error")
        });
    }
  };


  return (
    <Container component="main" maxWidth="xs" sx={{ marginTop: 20, marginBottom: 20 }}>
      <Paper elevation={2} sx={{ padding: 5 }} >
        <Typography component="h1" variant="h5" align='center'>
          LOGIN
        </Typography>
        <form onSubmit={login}>
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
            Sign In
          </Button>
        </form>
      </Paper>
    </Container>
  )
}

export default Login
