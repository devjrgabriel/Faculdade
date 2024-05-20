import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from './pages/home'
import Contato from './pages/contato'
import Erro from './pages/erro'
import Produto from "./pages/produto"
import Sobre from './pages/Sobre'
import Header from './components/Header'

export default function RouteApp(){
    return (
        <BrowserRouter>
            <Header/>
            <Routes>
                <Route path="/" element={<Home/>}/>
                <Route path="/Sobre" element={<Sobre/>}/>
                <Route path="/Contato" element={<Contato/>}/>
                <Route path="/Produto/:id" element={<Produto/>}/>
                <Route path="*" element={<Erro/>}/>
            </Routes>
        </BrowserRouter>
    )
}