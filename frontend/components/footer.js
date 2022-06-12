import React from "react";

import { FaCopyright } from "react-icons/fa";
import { FaYoutube } from "react-icons/fa";
import { FaInstagram } from "react-icons/fa";
import { FaHeart } from "react-icons/fa";
import styles from '../styles/Footer.module.css'
const Footer = () => {
  return (
    <footer className={styles.footer}>
      <div className="footer__social">
        <a href="https://www.instagram.com/speak.up.tech/">
          <FaInstagram size="40"  color="#fff"/>
        </a>
        <a href="https://www.youtube.com/c/SpeakupTech">
          <FaYoutube size="40"  color="#fff"/>
        </a>  
      </div>
      <p style={{color: 'white'}}>Made with by Speak up Tech<FaHeart color="#B51942"/>Hello</p>
    </footer>
  )
}
export default Footer 