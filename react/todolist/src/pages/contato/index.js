import { Link } from "react-router-dom";

export default function Contato() {
     return(
        <>
        <h1>Pagina Sobre o Contato </h1>
        <span>Act tecnologia</span>
        <Link to="/">Home</Link>
        <Link to="/Sobre">Sobre</Link>
        <hr/>
        <Link to="/produto/1">Acessar Produto</Link>
        </>
     );    
}