import { Link } from "react-router-dom";
import './header.css'

export default function Header() {
    return (
        <header>
            <div className="Navbar-js">
                <div className="imageNavbar"></div>
                <div className="navbarlist">

                    <Link className="Navitem" to="/">Home</Link>
                    <Link className="Navitem" to="/sobre">Sobre</Link>
                    <Link className="Navitem" to="/contato">Contato</Link>
                    <Link className="Navitem" to="/produto/1">Produto</Link>
                </div>

            </div>
        </header>
    )
}