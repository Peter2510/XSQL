import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CompilacionService {


  readonly URL = 'http://127.0.0.1:3000'

  constructor(private http: HttpClient) { }


  // metodo para enviar la info al server

  enviarInfo(data: string):Observable<string>{
    return this.http.post<string>(this.URL+"/compilar", JSON.stringify(data));
  }
}
