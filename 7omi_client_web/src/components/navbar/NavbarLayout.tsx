import React, { PropsWithChildren } from "react";
import Navbar from './Navbar'

function NavbarLayout({ children }: PropsWithChildren<{}>) {
  return (
    <>
      <Navbar />
      {children}
    </>
  )
}

export default NavbarLayout



