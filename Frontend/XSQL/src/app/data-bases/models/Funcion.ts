export class Funcion {
    id:string
    tipo: string;
    
    constructor(
        id:string,
        tipo:string,
    ) {
        this.id = id,
        this.tipo = tipo
    }

    toString() {
        return `Funcion ${this.id}, tipo ${this.tipo}`;
    }
}