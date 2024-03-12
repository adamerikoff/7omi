import { Container, Grid, Typography, Link, IconButton } from '@mui/material';

function Footer() {
  return (
    <Container maxWidth="lg" sx={{paddingTop:5}}>
      <Grid container spacing={3}>
        <Grid item xs={12} sm={6} md={3}>
          <Typography variant="h6">About 7omi</Typography>
          <Typography variant="subtitle2">
            We are a versatile communication tool designed to facilitate seamless and efficient interaction across various platforms. Whether you're chatting with friends, coordinating with colleagues, or staying connected with family, this app offers a unified and intuitive messaging experience.
          </Typography>
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <Typography variant="h6">Quick Links</Typography>
          <Typography variant="subtitle2">
            <Link href="/">Home</Link>
          </Typography>
          <Typography variant="subtitle2">
            <Link href="/login">Login</Link>
          </Typography>
          <Typography variant="subtitle2">
            <Link href="/register">Register</Link>
          </Typography>
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <Typography variant="h6">Social Links</Typography>
          <Typography variant="subtitle2">
            <Link href="/">Home</Link>
          </Typography>
          <Typography variant="subtitle2">
            <Link href="/login">Login</Link>
          </Typography>
          <Typography variant="subtitle2">
            <Link href="/register">Register</Link>
          </Typography>
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <Typography variant="h6">Contact Us</Typography>
          <Typography variant="subtitle2">City, Country</Typography>
          <Typography variant="subtitle2">123 Main Street</Typography>
          <Typography variant="subtitle2">info@example.com</Typography>
        </Grid>
      </Grid>
    </Container>
  )
}

export default Footer
