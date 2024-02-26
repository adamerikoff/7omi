import "./ContactList.css"


function ContactList() {
  const contacts = [
    { id: 1, name: 'John Doe' },
    { id: 2, name: 'Jane Smith' },
    { id: 3, name: 'Alice Johnson' },
    { id: 4, name: 'Bob Brown' },
  ];

  return (
    <div className="w-64  h-full">
      <div className="">
        <h1 className="text-white text-xl font-bold">searchbar</h1>
        <ul>
          {contacts.map((contact) => (
            <li key={contact.id}>
                {contact.name}
            </li>
          ))}
        </ul>
      </div>
    </div>
  )
}

export default ContactList