import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { EditorComponent } from '../editor-manager/editor.component';

@Component({
  selector: '.tab-pane[role=tabpanel]',
  templateUrl: './text-editor.component.html',
  styleUrls: ['./text-editor.component.css'],
})
export class TextEditorComponent implements OnInit, EditorComponent {
  @Input() data: any;
  content: string;
  line: number = 1;
  column: number = 1;

  constructor() {
    this.content = '';
    this.line = 1;
    this.column = 1;
  }

  @ViewChild('cm') cm: any;

  codeMirrorOptions: any = {
    theme: 'abcdef',
    mode:'text/x-mysql',
    lineNumbers: true,
    //lineWrapping: true,
    matchBrackets: true,
    autofocus: true,
    extraKeys: {
      Tab: function (cm: any) {
        cm.replaceSelection('    ', 'end');
      },
    },
  };

  ngOnInit(): void {
    this.content = this.data.initialContent;
  }


  ngAfterViewInit() {
    this.cm.cursorActivity.subscribe(this.caretMoved.bind(this));
  }

  onCompile() {

  }

  changeValues(line: number, column: number) {
    this.line = line;
    this.column = column;
  }

  caretMoved(codeMirror: any) {
    let cursor = codeMirror.getCursor();
    this.changeValues(cursor.line + 1, cursor.ch + 1);
  }
}
