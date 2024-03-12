import { ListItem, ListItemButton, ListItemText, Divider, Container } from "@mui/material"

import MessageTextField from "./MessageTextField"
import ChatHistory from "./ChatHistory"


function ChatWindow() {
  return (
    <Container disableGutters>
      <ChatHistory/>
      <MessageTextField/>
    </Container>
  )
}

export default ChatWindow
