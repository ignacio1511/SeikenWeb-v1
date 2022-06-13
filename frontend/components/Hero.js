import React from 'react'
import Link from 'next/link';
const Hero=(props)=>{
    return (
        <>
            <section className="sticky justify-center items-center">
                <img src = '/images/EntrenamientoSeikenEdit.png'/>
            
                <div className='absolute lg:pt-20 mt-10 pt-3 lg:mt-20 inset-0 justify-center items-center mx-10'>
                    <h1 className='text-center text-2xl lg:text-5xl text-white'> Transforma tu cuerpo entrenando 3 veces por semana y sin hacer dieta </h1>
                    <p className='text-center text-sm text-white container mt-3'>Somos Seiken, una comunidad de jovenes emprendedores que buscamos potenciar nuestra salud y condición física, sin dejar de lado nuestras demás responsabilidades. </p>
                    <Link href="#Datos-contactos">
                        <button type="submit" class="mt-4 mx-10 justify-center btn btn-primary bg-orange-700" name="action" valu="submit" data-toggle="button" aria-pressed="false" autocomplete="off">Descarga la rutina GRATIS</button> 
                    </Link>
                </div>
            </section>
        </>

    )
}
export default Hero;

