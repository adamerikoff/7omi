import "./ChatLayout.css"
import ChatWindow from "./chat_window/ChatWindow"
import ContactList from "./contact_list/ContactList"

function ChatLayout() {
  return (
    <div className="flex h-screen">
      <ContactList />
      <ChatWindow />
    </div>
  )
}

export default ChatLayout