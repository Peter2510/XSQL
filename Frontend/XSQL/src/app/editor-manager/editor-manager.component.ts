import {
  Component,
  ComponentRef,
  OnDestroy,
  OnInit,
  ViewChild,
} from '@angular/core';
import { table } from 'table';
import { TabHeaderComponent } from '../tab-header/tab-header.component';
import { TextEditorComponent } from '../text-editor/text-editor.component';
import { EditorItem } from './editor-item';
import {
  EditorComponent,
  ResultComponent,
  TabComponent,
} from './editor.component';
import { EditorDirective } from './editor.directive';
import { TabItem } from './tab-item';
import { TabDirective } from './tab.directive';
import SQLFile from 'src/analyze/SQLFile';

import { GraphvizService } from '../service/graphviz.service';
import { DomSanitizer, SafeUrl } from '@angular/platform-browser';
import { ResultDirective } from './result.directive';
import { ResultItem } from './result-item';
import { ResultImgComponent } from './result.component';
import { TableResultComponent } from './tableResult.component';
import { ThisReceiver } from '@angular/compiler';
import { CompilacionService } from '../service/compilacion.service';
import { ErrorSQL } from '../data-bases/models/Errors';
import { MatDialog } from '@angular/material/dialog';
import { ObtencionDBdumpComponent } from '../obtencion-dbdump/obtencion-dbdump.component';
import { NombreDBService } from '../service/nombre-db.service';
import { Simbolo, TablaSimbolo } from '../data-bases/models/TablaSimbolo';
import { Funcion } from '../data-bases/models/Funcion';

@Component({
  selector: 'app-editor-manager',
  templateUrl: './editor-manager.component.html',
  styleUrls: ['./editor-manager.component.css'],
})
export class EditorManagerComponent implements OnInit, OnDestroy {
  @ViewChild(EditorDirective, { static: true }) editorHost!: EditorDirective;
  @ViewChild(TabDirective, { static: true }) tabHost!: TabDirective;
  @ViewChild(ResultDirective, { static: true }) resultHost!: ResultDirective;

  @ViewChild('logger') logger: any;

  errores: ErrorSQL[] = [];
  tablas: TablaSimbolo[] = [];
  funciones: Funcion[] = [];
  mostrarTS = false
  mostrarTF = false

  codeMirrorOptions: any = {
    theme: 'dracula',
    lineNumbers: true,
    lineWrapping: false,
    matchBrackets: true,
    autofocus: false,
    readOnly: true,
  };

  contentLogger: string = '';
  editors: ComponentRef<EditorComponent>[] = [];
  tabs: ComponentRef<TabComponent>[] = [];
  names: string[] = [];
  filesToUpload: any[] = [];
  actualCode: any = null;
  currentDot: string = '';
  currentTac: string = '';
  name = ''
  animal = ''
  constructor(
    private service: GraphvizService,
    private sanitizer: DomSanitizer,
    private compilar: CompilacionService,
    private dialog: MatDialog,
    private servicioNombre: NombreDBService
  ) {}

  openDialog(): void {
    const dialogRef = this.dialog.open(ObtencionDBdumpComponent, {
      data: {name: this.name, animal: this.animal},
      width:'50%',
      height:"300px"
    });
    console.log(this.servicioNombre.getUsuario());

  }
  ngOnInit(): void {
    this.compilar.saludo().subscribe((info) => {
      console.log(info);
    });
  }


  graphvizImg(dot: string) {
    this.service.getImage(dot).subscribe({
      next: (response: any) => {
        let url = URL.createObjectURL(response);
        window.open(url, '_blank');
        URL.revokeObjectURL(url);
      },
      error: (e) => {
        console.error(e);
      },
    });
  }

  ngOnDestroy(): void {}

  ngAfterViewInit() {}

  onGetImage() {
    if (this.currentDot) {
      this.graphvizImg(this.currentDot);
    }
  }

  showSymbolTables(){
    this.mostrarTS = ! this.mostrarTS
  }

  showSymbolFunctions(){
    this.mostrarTF = ! this.mostrarTF
  }

  onGetTac() {
    this.contentLogger += this.currentTac;
  }

  onCompile() {
    let index = this.getActiveIndex();
    if (index !== -1) {
      let files: SQLFile[] = [];
      let main: SQLFile = new SQLFile(
        this.names[index],
        this.editors[index].instance.content
      );

      for (let i = 0; i < this.names.length; i++) {
        if (i !== index) {
          const name = this.names[i];
          const content = this.editors[i].instance.content;
          files.push(new SQLFile(name, content));
        }
      }

      //EJECUTAR EL ARCHIVO ACTUAL
      this.compilar.ejecutarSQL(main.content).subscribe((data) => {
        this.tablas = []
        this.funciones = []
        console.log(data);
        if (data.errores) {
          let errores = data.errores;
          let erroresJson = JSON.parse(errores);

          for (let i = 0; i < erroresJson.length; i++) {
            let error = erroresJson[i];
            let errorSQL = new ErrorSQL(
              error.tipo,
              error.token,
              error.descripcion,
              error.linea,
              error.columna
            );
            this.errores.push(errorSQL);
          }

          this.showErrorsConsole(this.errores);
        }
        if (data.resultados && data.resultados.length > 0) {
          const logs: string[] = [];
          data.resultados.forEach((res: any) => {
            if (res.tipo === 'select') {
              logs.push(this.getSelectFormat(res.resultado));
            } else {
              logs.push(res.resultado);
            }
          });

          this.showLogs(logs);
        }

        if (data.dot) {
          this.currentDot = data.dot;
        } else {
          this.currentDot = '';
        }

        if(data.tac) {
          this.currentTac = data.tac
        } else {
          this.currentTac = '';
        }

        if (data.tablas) {
          let tbl = data.tablas;
          let tablasJson = JSON.parse(tbl);

          for (let i = 0; i < tablasJson.length; i++) {

            let tabla = tablasJson[i];
            let TS = new TablaSimbolo(tabla.Entorno,[])
            let datos = []

            for (let j = 0; j < tabla.datos.length; j++) {

              let simbolo = tabla.datos[j]
              let sim = new Simbolo(simbolo.id,simbolo.tipo,simbolo.valor)
              datos.push(sim)

            }
            TS.datos = datos
            this.tablas.push(TS)


          }




        }

        if (data.funciones) {

          let ftcs = data.funciones;
          let funcinesJson = JSON.parse(ftcs);

          for (let i = 0; i < funcinesJson.length; i++) {

            let funcion = funcinesJson[i];

            this.funciones.push(new Funcion(funcion.nombre,funcion.tipo))
          }
          console.log(this.funciones)
        }

      });

      // this.resultHost.viewContainerRef.clear();
    }
  }

  getSelectFormat(results: [][]) {
    return table(results);
  }

  showLogs(logs: any[]) {
    logs.forEach((l) => (this.contentLogger += l + '\n'));
  }
  showErrorsConsole(errors: any[]) {
    errors.forEach((e) => (this.contentLogger += e.toString() + '\n'));
    this.errores = [];
  }

  clearLogger() {
    this.contentLogger = '';
    this.currentDot = '';
    this.tablas = []
    this.funciones = []
  }

  clearResults() {
    this.resultHost.viewContainerRef.clear();
  }

  showTables(tables: any[]) {
    const viewContainerRef = this.resultHost.viewContainerRef;
    tables.forEach((info) => {
      const resultItem = new ResultItem(TableResultComponent, info);
      const resultComponent = viewContainerRef.createComponent<ResultComponent>(
        resultItem.component
      );
      resultComponent.instance.data = resultItem.data;
    });
  }

  addBlankEditor(name: string, content: string = '') {
    let nameTab = `${name}-tab`;
    let target = '#' + name;

    this.names.push(name);

    const editorItem = new EditorItem(TextEditorComponent, {
      id: name,
      label: nameTab,
      initialContent: content,
    });
    const viewContainerRef = this.editorHost.viewContainerRef;

    const componentRef = viewContainerRef.createComponent<EditorComponent>(
      editorItem.component
    );
    componentRef.instance.data = editorItem.data;
    const element = componentRef.location.nativeElement;

    // element.setAttribute('aria-labelledby', editorItem.data.label);
    element.classList.add('active');
    element.id = editorItem.data.id;
    const tabViewContainerRef = this.tabHost.viewContainerRef;
    const tabItem = new TabItem(TabHeaderComponent, {
      name: nameTab,
      target: target,
      pane: name,
    });

    const componentRefTab = tabViewContainerRef.createComponent<TabComponent>(
      tabItem.component
    );

    const elementTab = componentRefTab.location.nativeElement;
    elementTab.firstChild.classList.add('active');
    componentRefTab.instance.data = tabItem.data;

    // Remove class list
    this.tabs.forEach((t) =>
      t.location.nativeElement.firstChild.classList.remove('active')
    );
    this.editors.forEach((t) =>
      t.location.nativeElement.classList.remove('active')
    );
    //

    this.tabs.push(componentRefTab);
    this.editors.push(componentRef);
  }

  closeActualEditor() {
    let index = this.getActiveIndex();

    if (index !== -1 && confirm('¿Deseas cerrar la pestaña actual?')) {
      this.names.splice(index, 1);
      let editor = this.editors.splice(index, 1);
      let tab = this.tabs.splice(index, 1);
      const viewContainerRef = this.editorHost.viewContainerRef;
      let editI = viewContainerRef.indexOf(editor[0].hostView);
      const viewContainerRefTab = this.tabHost.viewContainerRef;
      let tabI = viewContainerRefTab.indexOf(tab[0].hostView);

      viewContainerRef.remove(editI);
      viewContainerRefTab.remove(tabI);
    }
  }

  getName() {
    let name = prompt('Nombre del archivo');
    name = (name as string).replace(' ', '');
    let regex = /^[a-zA-z](\d|[a-zA-z])*$/;
    if (name.match(regex) && !this.isRepeatedName(name)) {
      this.addBlankEditor(name);
    } else {
      alert('Nombre inválido');
    }
  }

  isRepeatedName(searchedName: string): boolean {
    return this.names.findIndex((name) => name === searchedName) !== -1;
  }

  uploadFile(event: any) {
    if (event.target.files.length > 0) {
      this.filesToUpload = event.target.files;
    }
  }

  readFile() {
    if (this.filesToUpload.length > 0) {
      let files = this.filesToUpload;
      // console.log(files);
      for (const file of files) {
        let name = file.name.replace('.sql', '');
        console.log(name);
        if (!this.isRepeatedName(name)) {
          let reader = new FileReader();
          const freader = () => {
            this.actualCode = reader.result as string;
            console.log(this.actualCode, 'jhs');
            if (this.actualCode) {
              reader.removeEventListener('load', freader);
              this.addBlankEditor(name, this.actualCode);
              this.actualCode = null;
              this.filesToUpload = [];
            }
          };
          reader.addEventListener('load', freader, false);

          reader.onerror = function (evt) {};
          reader.readAsText(file, 'UTF-8');
        } else {
          alert('Nombre repetido');
        }
      }
    } else {
      alert('Error al leer el archivo');
    }
  }

  download() {
    let index = this.getActiveIndex();
    if (index !== -1) {
      let editor = this.editors[index];
      let name = this.names[index] + '.sql';
      let file = new Blob([editor.instance.content], { type: 'text' });
      let a = document.createElement('a'),
        url = URL.createObjectURL(file);
      a.href = url;
      a.download = name;
      document.body.appendChild(a);
      a.click();
      setTimeout(function () {
        document.body.removeChild(a);
        window.URL.revokeObjectURL(url);
      }, 0);
    }
  }

  getActiveIndex() {
    let index = this.editors.findIndex((editorRef) => {
      return editorRef.location.nativeElement.classList.contains('active');
    });
    return index;
  }

  generarDump() {
    let index = this.getActiveIndex();
    if (index !== -1) {
      this.compilar.generaDump(this.servicioNombre.getUsuario()).subscribe((text: any) => {
        console.log(text);

        let name = this.names[index] + '.sql';
        let file = new Blob([text], { type: 'text' });
        let a = document.createElement('a'),
          url = URL.createObjectURL(file);
        a.href = url;
        a.download = name;
        document.body.appendChild(a);
        a.click();
        setTimeout(function () {
          document.body.removeChild(a);
          window.URL.revokeObjectURL(url);
        }, 0);
      });
    }
  }

  expotarInserts() {
    let index = this.getActiveIndex();
    if (index !== -1) {
      this.compilar.generaExport(this.servicioNombre.getUsuario()).subscribe((text: any) => {
        console.log(text);

        let name = this.names[index] + '.sql';
        let file = new Blob([text], { type: 'text' });
        let a = document.createElement('a'),
          url = URL.createObjectURL(file);
        a.href = url;
        a.download = name;
        document.body.appendChild(a);
        a.click();
        setTimeout(function () {
          document.body.removeChild(a);
          window.URL.revokeObjectURL(url);
        }, 0);
      });
    }
  }
}
