import React from 'react'
import { TbBrandMeta } from 'react-icons/tb'
import { IoLogoInstagram } from 'react-icons/io'
import { RiTwitterXLine } from 'react-icons/ri'

const TopBar = () => {
  return (
    <div className="bg-[#ea2e0e] text-white text-sm py-2">
      <div className="container mx-auto px-4">
        <div className="flex items-center space-x-4">
          <a href="#" className="hover:text-gray-300 text-decoration-none">
            <TbBrandMeta className="h-5 w-5" style={{ fontSize: '20px' }} />
          </a>
          <a href="#" className="hover:text-gray-300 text-decoration-none">
            <IoLogoInstagram className="h-5 w-5" style={{ fontSize: '20px' }} />
          </a>
          <a href="#" className="hover:text-gray-300 text-decoration-none">
            <RiTwitterXLine className="h-5 w-5" style={{ fontSize: '20px' }} />
          </a>
        </div>

        <div className="text-center mt-2">
          <span>we ship world wide - fast and stuff</span>
        </div>

        <div className="mt-2">
          <a href="tel:+12345678" className="hover:text-gray-300 text-decoration-none">
            +123456789
          </a>
        </div>
      </div>
    </div>
  )
}

export default TopBar
