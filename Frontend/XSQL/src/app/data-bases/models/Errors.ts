export class ErrorSQL {
    // Define las propiedades de la clase
    tipo: string;
    token: any;
    descripcion: string;
    linea: number;
    columna: number;

    // Asigna los parámetros del constructor a las propiedades
    constructor(
        tipo: string,
        token: any,
        descripcion: string,
        linea: number,
        columna: number
    ) {
        this.tipo = tipo;
        this.token = token;
        this.descripcion = descripcion;
        this.linea = linea;
        this.columna = columna;
    }

    // Implementa el método toString
    toString() {
        return `Error ${this.tipo}, Token: ${this.token}, ${this.descripcion} en la línea ${this.linea} y columna ${this.columna}`;
    }
}