import { List, ListItem, ListItemButton, ListItemText } from "@mui/material"

import ConversationItem from "./ConversationItem"

function Conversations() { 
  const conversations = [
    {
      title: "Conversation 1",
      latestMessage: "Latest message in conversation 1",
    },
    {
      title: "Conversation 2",
      latestMessage: "Latest message in conversation 2",
    },
    {
      title: "Conversation 2",
      latestMessage: "Latest message in conversation 2",
    },
    {
      title: "Conversation 2",
      latestMessage: "Latest message in conversation 2",
    },
    {
      title: "Conversation 2",
      latestMessage: "Latest message in conversation 2",
    },
    {
      title: "Conversation 2",
      latestMessage: "Latest message in conversation 2",
    },
    {
      title: "Conversation 2",
      latestMessage: "Latest message in conversation 2",
    },
    {
      title: "Conversation 1",
      latestMessage: "Latest message in conversation 1",
    },
    {
      title: "Conversation 2",
      latestMessage: "Latest message in conversation 2",
    },
    {
      title: "Conversation 2",
      latestMessage: "Latest message in conversation 2",
    },
    {
      title: "Conversation 2",
      latestMessage: "Latest message in conversation 2",
    },
    {
      title: "Conversation 2",
      latestMessage: "Latest message in conversation 2",
    },
    {
      title: "Conversation 2",
      latestMessage: "Latest message in conversation 2",
    },
    {
      title: "Conversation 2",
      latestMessage: "Latest message in conversation 2",
    },
  ];

  return (
    <List sx={{ padding: 0, margin: 0, maxHeight: '70vh', overflow: 'auto' }}>
      {/* Map over the array of conversations and render ConversationItem for each */}
      {conversations.map((conversation, index) => (
        <ConversationItem key={index} title={conversation.title} latestMessage={conversation.latestMessage}/>
      ))}
    </List>
  )
}

export default Conversations
