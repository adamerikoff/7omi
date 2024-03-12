import { useEffect } from 'react'
import { Link, useNavigate } from 'react-router-dom';

import { Container, Grid } from '@mui/material';
import axios from 'axios';

import { fetchToken } from '../services/Auth';

import Conversations from '../components/Conversation'
import ChatWindow from '../components/ChatWindow'

function Chat() {
  return (
    <Container>
      <Grid container spacing={0}>
        <Grid item xs={4}>
          <Conversations/>
        </Grid>
        <Grid item xs={8}>
          <ChatWindow/>
        </Grid>
      </Grid>
    </Container>
  )
}

export default Chat
