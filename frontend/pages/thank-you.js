import Container from '../components/Container'
import React from 'react'
import { FaCheckCircle } from "react-icons/fa";

const ThankYou = () => {
  return (
    <>
    <div className="">
      <Container titulo="thank-you">

          <section className='grid place-items-center mt-4'>
              <FaCheckCircle size="100" color='#008000'/>
          </section>

          <section className='grid place-items-center mt-4'>
              <h1 className='text-xl text-center'>¡Felicitaciones! Tu rutina va en camino.</h1>
              <p className='text-xs mt-2 text-center'> Revisa tu bandeja de entrada. La rutina tardará a lo mucho 5 minutos en llega.</p>
              <b><p className='text-xs mt-2 text-center'>¡A darle con todo!</p></b>
          </section>

      </Container>
    </div>
    </>
  )
}

export default ThankYou;


// https://react-icons.github.io/react-icons/icons?name=fa