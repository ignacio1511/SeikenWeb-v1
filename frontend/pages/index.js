import Contact from '../components/Contact'
import Container from '../components/Container'
import Hero from '../components/Hero'
import {useEffect} from 'react'
import {useRouter} from 'next/router'

const Home = ({posts})=> {

    
    return (
        <>
        {console.log(posts)}
        <div>
            <Container titulo="Seiken">
            <Hero />
            <Contact />
            </Container>
        </div>

        </>
    )
}


export async function getStaticProps(){
    const res = await fetch("http://127.0.0.1:8000/api/user-list")
    const posts = await res.json();

    return{
        props:{
            posts
        },
    };
}

export default Home