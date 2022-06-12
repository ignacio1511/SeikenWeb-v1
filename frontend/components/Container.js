import Head from 'next/head'
import Link from 'next/link';
import Navigation from './navigation'
import Footer from './footer'
import Hero from './Hero'

const Container = ({titulo,children}) =>(
    
    <div>
        <Head>
        <link rel="shortcut icon" href="/images/favicon.ico"/>
        <title>{titulo}</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <script src="https://kit.fontawesome.com/448126ce4f.js" crossorigin="anonymous"></script> 
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/united/bootstrap.min.css" />            
        </Head>
        <Navigation/>
        <div>
            {children}
        </div>
 
    </div>
)
export default Container;