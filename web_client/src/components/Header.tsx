import { useState } from 'react'

import { Link } from 'react-router-dom'

import { AppBar, Container, Typography, Box, Menu, Button, Toolbar, Grid } from '@mui/material'
import { fetchToken, removeToken } from '../services/Auth'

function Header() {
  const [isLoggedIn, setIsLoggedIn] = useState(!!fetchToken())
  const handleLogout = () => {
    removeToken()
    setIsLoggedIn(!isLoggedIn)
  };

  return (
    <AppBar position="static">
      <Container>
        <Toolbar>
          <Grid container spacing={2} alignItems="center">
            <Grid item xs={2}>
              <Button component={Link} to="/" variant="text" color="inherit">
                7omi
              </Button>
            </Grid>
            <Grid item xs={6}>
              {/* Empty grid item for center alignment */}
            </Grid>
            <Grid item xs={4} container justifyContent="flex-end">
              <Button component={Link} to="/" variant="text" color="inherit">
                Home
              </Button>
              {
                isLoggedIn ? (
                  <>
                  <Button component={Link} to="/login" variant="contained" color="error" onClick={handleLogout}>
                    Logout
                  </Button>
                  </>
                ) : (
                  <>
                  <Button component={Link} to="/login" variant="text" color="inherit">
                    Login
                  </Button>
                  <Button component={Link} to="/register" variant="text" color="inherit">
                    Register
                  </Button>
                  </>
                )
              }
            </Grid>
          </Grid>
        </Toolbar>
      </Container>
    </AppBar>
  )
}

export default Header
