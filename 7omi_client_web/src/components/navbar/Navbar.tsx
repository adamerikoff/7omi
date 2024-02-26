import {Link} from 'react-router-dom';

import './Navbar.css'

function Navbar() {
  return (
    <nav className='w-screen bg-sky-500'>
      <div className='flex justify-center'>
        <Link to="/" className="mx-4 text-white">Home</Link>
        <Link to="/about" className="mx-4 text-white">About</Link>
        <Link to="/contacts" className="mx-4 text-white">Contacts</Link>
      </div>
    </nav>
  )
}

export default Navbar



