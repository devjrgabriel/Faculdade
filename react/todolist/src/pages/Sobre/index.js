import { Link } from "react-router-dom";

export default function Sobre() {
     return(
        <>
        <h1>Pagina Sobre a empresa </h1>
        <span>Act tecnologia</span>
        <Link to="/">Home</Link>
        <Link to="/Contato">Contato</Link>
        <hr/>
        <Link to="/produto/1">Acessar Produto</Link>
        </>
     );    
}