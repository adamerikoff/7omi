import {Link} from 'react-router-dom';

import './Navbar.css'

function Navbar() {
  return (
    <nav className='w-full bg-indigo-600'>
      <div className="container mx-auto px-4 py-2 flex justify-between items-center">
        <a className="font-bold text-2xl lg:text-4xl text-white" href="#">
          7omi
        </a>
        <div className="hidden lg:block">
          <ul className="flex">
            <li className="mr-4">
              <Link to="/" className="text-white">Home</Link>
            </li>
            <li className="mr-4">
              <Link to="/about" className="text-white">About</Link>
            </li>
            <li className="mr-4">
              <Link to="/contacts" className="text-white">Contacts</Link>
            </li>
            <li className="mr-4">
              <Link to="/signup" className="text-white">Signup</Link>
            </li>
            <li>
              <Link to="/login" className="text-white">Login</Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  )
}

export default Navbar



