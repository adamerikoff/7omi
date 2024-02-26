import {Link} from 'react-router-dom';



function Footer() {
  return (
    <footer className="bg-gray-100">
      <div className="container mx-auto px-6 pt-10 pb-6">
        <div className="flex flex-wrap">
          <div className="w-full md:w-1/4 text-center md:text-left">
            <h5 className="uppercase mb-6 font-bold">Links</h5>
            <ul className="mb-4">
              <li className="mt-2">
                <Link to="/home" className="hover:underline text-gray-600 hover:text-orange-500">FAQ</Link>
              </li>
              <li className="mt-2">
                <Link to="/home" className="hover:underline text-gray-600 hover:text-orange-500">Home</Link>
              </li>
              
            </ul>
          </div>
          <div className="w-full md:w-1/4 text-center md:text-left">
            <h5 className="uppercase mb-6 font-bold">Social</h5>
            <ul className="mb-4">
              <li className="mt-2">
                <a href="#" className="hover:underline text-gray-600 hover:text-orange-500">Facebook</a>
              </li>
              <li className="mt-2">
                <a href="#" className="hover:underline text-gray-600 hover:text-orange-500">Linkedin</a>
              </li>
              <li className="mt-2">
                <a href="#" className="hover:underline text-gray-600 hover:text-orange-500">GitHub</a>
              </li>
            </ul>
          </div>
          <div className="w-full md:w-1/4 text-center md:text-left">
            <h5 className="uppercase mb-6 font-bold">Company</h5>
            <ul className="mb-4">
              <li className="mt-2">
                <a href="#" className="hover:underline text-gray-600 hover:text-orange-500">Official Blog</a>
              </li>
              <li className="mt-2">
                <Link to="/about" className="hover:underline text-gray-600 hover:text-orange-500">About Us</Link>
              </li>
              <li className="mt-2">
                <Link to="/contacts" className="hover:underline text-gray-600 hover:text-orange-500">Contacts</Link>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </footer>
  )
}

export default Footer



