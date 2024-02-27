import "./ChatWindow.css"

function ChatWindow() {
  const messages = [
    "afasklfnaklfs",
    "fasnflkanklfsnal"
  ]
  return (
    <div className="flex flex-col w-full border border-gray-300 overflow-hidden">
      <div className="flex-1 p-4 overflow-y-auto">
        {messages.map((message, index) => (
          <div key={index} className="mb-2">
            {message}
          </div>
        ))}
      </div>
      <div className="flex items-center p-4 border-t border-gray-300 w-full">
        <input type="text" placeholder="..." className="flex-1  p-2"/>
        <button className="bg-blue-500 text-white px-4 py-2 ml-2"> Send </button>
      </div>
    </div>
  )
}

export default ChatWindow