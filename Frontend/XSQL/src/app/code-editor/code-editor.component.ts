import { Component, OnInit } from '@angular/core';
import { CodeModel } from '@ngstack/code-editor';
import { CompilacionService } from '../services/compilacion.service';

@Component({
  selector: 'app-code-editor',
  templateUrl: './code-editor.component.html',
  styleUrls: ['./code-editor.component.css']
})
export class CodeEditorComponent implements OnInit{

  theme = 'vs-dark';

  codeModel: CodeModel = {
    language: 'sql',
    uri: 'main.sql',
    value: ''
  };

  options = {
    contextmenu: true,
    minimap: {
      enabled: false
    }, fontSize: 15
  };


  valor:any
  constructor(private servicio:CompilacionService){}


  enviarData(){
    this.servicio.enviarInfo("simon").subscribe();

  }
  ngOnInit(): void {
  }
}
