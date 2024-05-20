import {Link} from 'react-router-dom'

export default function Erro() {
    return(
        <div>
            <h2>A o lagarto</h2>
            <span>Encontramos estas paginas aqui:</span>
            <Link to='/'>Home</Link>
            <Link to='/sobre'>Sobre</Link>
            <Link to='/contato'>Contato</Link>
        </div>
    )
    
}