import React, {Component} from "react";
import './style.css'
import cronometro from './assets/cronometro.png'

class App  extends Component{
  constructor(props){
    super(props)
    this.state = {
      numero : 0,
      botao: 'INICIAR'
    }
    this.timer = null;
  }
}
