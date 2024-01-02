export class TablaSimbolo {
    entorno: string;
    datos: Simbolo[]
    
    constructor(
        entorno:string,
        datos:[]
    ) {
        this.entorno = entorno
        this.datos = datos
    }

    toString() {
        return `Entorno ${this.entorno}, datos ${this.datos}`;
    }
}

export class Simbolo {
    id:string
    tipo: string;
    valor: string;
    
    constructor(
        id:string,
        tipo:string,
        valor:string,
    ) {
        this.id = id,
        this.tipo = tipo,
        this.valor = valor        
    }

    toString() {
        return `Simbolo ${this.id}, tipo ${this.tipo}, valor ${this.valor}`;
    }
}