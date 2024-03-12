import { ListItem, ListItemButton, ListItemText, Divider, Container } from "@mui/material"

import Message from "./Message"

function ChatWindow() {
  const messages = [
    { author: "admin", text: "Hello!" },
    { author: "otherUser", text: "Hi there!" },
    { author: "admin", text: "How are you?" },
    { author: "otherUser", text: "I'm good, thanks!" },
    { author: "admin", text: "Hello!" },
    { author: "otherUser", text: "Hi there!" },
    { author: "admin", text: "How are you?" },
    { author: "otherUser", text: "I'm good, thanks!" },
    { author: "admin", text: "Hello!" },
    { author: "otherUser", text: "Hi there!" },
    { author: "admin", text: "How are you?" },
    { author: "otherUser", text: "I'm good, thanks!" },
    { author: "admin", text: "Hello!" },
    { author: "otherUser", text: "Hi there!" },
    { author: "admin", text: "How are you?" },
    { author: "otherUser", text: "I'm good, thanks!" },
    { author: "admin", text: "Hello!" },
    { author: "otherUser", text: "Hi there!" },
    { author: "admin", text: "How are you?" },
    { author: "otherUser", text: "I'm good, thanks!" },
  ];
  return (
    <Container disableGutters sx={{ padding: 0, margin: 0, maxHeight: '70vh', overflow: 'auto' }}>
      {messages.map((message, index) => (
        <Message key={index} author={message.author} text={message.text}/>
      ))}
    </Container>
  )
}

export default ChatWindow
