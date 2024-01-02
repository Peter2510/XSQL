import { Component, OnInit } from '@angular/core';
import { TreeNode, TreeModel, TREE_ACTIONS, KEYS, IActionMapping, ITreeOptions } from '@bugsplat/angular-tree-component';
import { CompilacionService } from '../service/compilacion.service';

const actionMapping: IActionMapping = {
  mouse: {
    contextMenu: (tree, node, $event) => {
      $event.preventDefault();
      //SELECCION DEL TEXTO DEL NODO


    },
    dblClick: (tree, node, $event) => {
      if (node.hasChildren) {
        TREE_ACTIONS.TOGGLE_EXPANDED(tree, node, $event);
      }
    },
    click: (tree, node, $event) => {
      $event.shiftKey
        ? TREE_ACTIONS.TOGGLE_ACTIVE_MULTI(tree, node, $event)
        : TREE_ACTIONS.TOGGLE_ACTIVE(tree, node, $event);
    }
  }
};

@Component({
  selector: 'app-data-bases',
  templateUrl: './data-bases.component.html',
  styleUrls: ['./data-bases.component.css']
})
export class DataBasesComponent implements OnInit {

  arregloDB:any
  valor:any
  nodes: any[] = [];
  constructor(private obtenerDBservicio: CompilacionService) { }

  ngOnInit(): void {
    this.obtenerDBservicio.saludo().subscribe(
        elementos => {
          this.arregloDB = elementos
          console.log(this.arregloDB[0]?.tables[0]?.data?.estructura?.idfactura);

          this.generarNodos()
        }
      )


  }


  generarNodos(){
    const jsonObjects = this.arregloDB.map((element: any, index: number) => ({
      id: index + 1, // Se puede utilizar el índice + 1 como ID
      name: element['name'] // Suponiendo que cada elemento tiene una propiedad 'name'
      //
  }));

  // El arreglo 'jsonObjects' contendrá un JSON por cada elemento en 'this.arregloDB'
  console.log(jsonObjects);
    this.nodes = jsonObjects;
  }





  options: ITreeOptions = {
    actionMapping
  };

}
