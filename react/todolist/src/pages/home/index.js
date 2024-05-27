import { Link } from "react-router-dom";

export default function Home() {
     return(
        <>
        <h1>Bem vindo a pagina Home </h1>
        <span>Gabriel Souza</span>
        <Link to="/sobre">Sobre</Link>
        <Link to="/Contato">Contato</Link>
        <hr/>
        <Link to="/produto/1">Acessar Produto</Link>
        </>
     )

    
}