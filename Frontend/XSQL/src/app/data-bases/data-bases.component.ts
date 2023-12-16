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
    this.nodes = [
      {
        id: 1,
        name: this.arregloDB[0]["name"],
        children: [
          { id: 2, name: this.arregloDB[0]["tables"][0]["name"] },
          { id: 3, name: this.arregloDB[0]["tables"][1]["name"] },
          {
            id: 4,
            name: this.arregloDB[0]["tables"][0]["data"]["estructura"]["nombrecliente"]["nombre"],
            children: [
              { id: 5, name: this.arregloDB[0]["tables"][0]["data"]["estructura"]["nombrecliente"]["caracteristicas"]["Atributo1"]["tipo"]}
            ]
          }
        ]
      },
      {
        id: 6,
        name: 'root2',
        children: [
          { id: 7, name: 'child2.1' },
          {
            id: 8,
            name: 'child2.2',
            children: [
              { id: 9, name: 'subsub' }
            ]
          }
        ]
      }
    ];
  }





  options: ITreeOptions = {
    actionMapping
  };

}
