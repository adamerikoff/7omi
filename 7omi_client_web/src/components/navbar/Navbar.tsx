import {Link} from 'react-router-dom';

import './Navbar.css'

function Navbar() {
  return (
    <nav className='container'>
      <div className='flex justify-center'>
      <Link to="/" className="mx-4 text-white">Home</Link>
        <Link to="/about" className="mx-4 text-white">About</Link>
        <Link to="/services" className="mx-4 text-white">Services</Link>
        <Link to="/contact" className="mx-4 text-white">Contact</Link>
        <Link to="/blog" className="mx-4 text-white">Blog</Link>
      </div>
    </nav>
  )
}

export default Navbar



