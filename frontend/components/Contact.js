import React, {useState} from 'react'
import Axios from 'axios'

export default function Contact() {

    const [first_name, setName] = useState('')
    const [last_name, setLastName] = useState('')
    const [email, setEmail] = useState('')
    const [objetivo, setObjetivo] = useState('perder_grasa')


    const handleSubmit = (e) => {
        e.preventDefault();
        const usuario = {first_name, last_name, email, objetivo};

        fetch('http://127.0.0.1:8000/api/user-create/', {
            method : 'POST',
            headers: {"Content-Type" : "application/json"},
            body: JSON.stringify(usuario),
        }). then(() => {
            console.log("Nuevo usuario añadido")
            console.log(usuario)
        })
    } 
    

  return (
    
    <section className='mt-4'>
        <div className='mx-10'>
            <h1 className='text-center text-xl'>Descarga nuestra rutina de entrenamiento en casa 3 veces por semana gratis </h1>

            <img className ="mt-3" src='/images/ebookCover.png' />
        
            <label class="block mt-4">
                <form onSubmit={handleSubmit}>

                    <span 
                    class="after:content-['*'] after:ml-0.5 after:text-red-500 block text-sm font-medium text-slate-700">
                        Nombre
                    </span>

                    <input type="text" 
                    required 
                    name="first_name" 
                    className="mt-1 px-3 py-2 bg-white border shadow-sm border-slate-300 placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-sky-500 block w-full rounded-md sm:text-sm focus:ring-1" 
                    value={first_name} 
                    onChange={(e) => setName(e.target.value)}
                    />

                    <span 
                    class="mt-1 after:content-['*'] after:ml-0.5 after:text-red-500 block text-sm font-medium text-slate-700">
                        Apellido
                    </span>

                    <input 
                    type="text" 
                    required 
                    name="last_name" 
                    className="mt-1 px-3 py-2 bg-white border shadow-sm border-slate-300 placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-sky-500 block w-full rounded-md sm:text-sm focus:ring-1" 
                    value={last_name} 
                    onChange={(e) => setLastName(e.target.value)}
                    />

                    <span 
                    class="mt-1 after:content-['*'] after:ml-0.5 after:text-red-500 block text-sm font-medium text-slate-700">
                        Correo electronico
                    </span>

                    <input 
                    type="email" 
                    required 
                    name="email" 
                    className="mt-1 px-3 py-2 bg-white border shadow-sm border-slate-300 placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-sky-500 block w-full rounded-md sm:text-sm focus:ring-1" 
                    value={email} 
                    onChange={(e) => setEmail(e.target.value)}
                    />


                    <span 
                    class="mt-1 after:content-['*'] after:ml-0.5 after:text-red-500 block text-sm font-medium text-slate-700">
                        ¿Cual es tu objetivo?
                    </span>

                    <select 
                    className="mt-1 px-3 py-2 bg-white border shadow-sm border-slate-300 placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-sky-500 block w-full rounded-md sm:text-sm focus:ring-1"
                    value={objetivo} 
                    onChange={(e) => setObjetivo(e.target.value)}
                    >
                        <option type="text" value="perder_grasa" >Quiero bajar de peso lo antes posible</option>
                        <option type="text" value="ganar_musculo">Quiero ganar músculo aceleradamente</option>
                        <option type="text" value="ambos">Quiero definir mi cuerpo</option>
                    </select>

                    {<button onClick={handleSubmit}
                    class="mt-3 mb-4 btn btn-primary bg-orange-700"
                    >Descarga la rutina GRATIS
                    </button>}


                </form>
                
            </label>
        </div>
    </section>

  )
}
