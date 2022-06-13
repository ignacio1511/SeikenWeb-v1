import React from "react";

import { BsFillCheckSquareFill } from "react-icons/fa";
import { FaYoutube } from "react-icons/fa";
import { FaInstagram } from "react-icons/fa";
import { FaHeart } from "react-icons/fa";
import styles from '../styles/Footer.module.css'
const Footer = () => {
  return (
<footer class="p-4 bg-white rounded-lg shadow md:px-6 md:py-8 dark:bg-gray-800">
    <div class="sm:flex sm:items-center sm:justify-between">
    </div>
    <hr class="my-6 border-gray-200 sm:mx-auto dark:border-gray-300 lg:my-8" />
    <span class="block text-sm text-gray-500 sm:text-center dark:text-gray-400">© 2022 Seiken™. Todos los derechos reservados.
    </span>
</footer>
  )
}
export default Footer 

