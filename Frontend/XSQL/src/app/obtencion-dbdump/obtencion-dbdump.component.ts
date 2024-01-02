import { Component, ElementRef, Inject, ViewChild } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { EditorManagerComponent } from '../editor-manager/editor-manager.component';
import { NombreDBService } from '../service/nombre-db.service';

@Component({
  selector: 'app-obtencion-dbdump',
  standalone: true,
  imports: [],
  templateUrl: './obtencion-dbdump.component.html',
  styleUrl: './obtencion-dbdump.component.css'
})
export class ObtencionDBdumpComponent {
  @ViewChild('nombreInput') nombreInput: ElementRef;
  prueba:any
  constructor(
    public dialogRef: MatDialogRef<EditorManagerComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any,
    private servicioDb: NombreDBService
  ) {}
  definicionDB():void{
    const nombreValue = this.nombreInput.nativeElement.value;
    // Use the value as needed
    console.log(nombreValue);
    this.servicioDb.setUsuario(nombreValue);
    console.log(
    this.servicioDb.getUsuario())
  }
  onNoClick(): void {
    this.dialogRef.close();
  }


}
