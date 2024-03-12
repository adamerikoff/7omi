import { ListItem, ListItemButton, ListItemText, Divider } from "@mui/material"

interface Props {
  title: string;
  latestMessage: string;
}


function ConversationItem({ title, latestMessage }: Props) {
  return (
    <>
      <Divider variant="middle" />
      <ListItem disablePadding>
        <ListItemButton>
          <ListItemText primary={title} secondary={latestMessage} />
        </ListItemButton>
      </ListItem>
      <Divider variant="middle" />
    </>
  )
}

export default ConversationItem
