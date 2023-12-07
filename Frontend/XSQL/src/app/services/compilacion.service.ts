import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

const baseURL = "http://localhost:3000";

@Injectable({
  providedIn: 'root'
})
export class CompilacionService {

  constructor(private http: HttpClient) { }

  // metodo para enviar la info al server

  public ejecutarSQL(data: any): Observable<any> {

    return this.http.post<any>(`${baseURL}/ejecutar`, JSON.stringify(data));
      
  }

  saludo():Observable<any>{
     return this.http.get<any>(`${baseURL}`+"/saludo");
   }

}
