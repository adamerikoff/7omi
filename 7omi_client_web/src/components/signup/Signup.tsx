import React, { useState } from 'react';

import './Signup.css'

function Signup() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleEmailChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setPassword(e.target.value);
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    // Here you can handle form submission, such as sending the data to a server or validating it
    console.log('Email:', email);
    console.log('Password:', password);
  };

  return (
    <form className="flex min-h-full flex-col justify-center px-6 py-12" onSubmit={handleSubmit}>
      <div className="">
        <img className="mx-auto h-20 w-auto" src="./logo.png" alt="7omi" />
        <h2 className="text-center text-2xl font-bold">Register yourself</h2>
      </div>
      <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <div className="my-2">
          <label htmlFor="email">Email:</label>
          <input className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" type="email" id="email" value={email} onChange={handleEmailChange} required />
        </div>
        <div className="my-2">
          <label htmlFor="email">Password:</label>
          <input className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" type="password" id="password" value={password} onChange={handlePasswordChange} required />
        </div>
        <button className="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600" type="submit">Register</button>
      </div>
    </form>
  )
}

export default Signup




