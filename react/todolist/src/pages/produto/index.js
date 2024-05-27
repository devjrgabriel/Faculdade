import { Link } from "react-router-dom";
import { useParams } from "react-router-dom";
export default function Produtos(){
    const {id} = useParams();
    return(
        <div>
            <h2>Pagina - Detalhe Produtos</h2>
            <span>
                Meu produto é {id}
            </span>
        </div>
    )
}