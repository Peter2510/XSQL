import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { BehaviorSubject, Observable, map } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class NombreDBService {

  private nombre: string | null = null;

  private user = new BehaviorSubject<string | null>(null);
  user$ = this.user.asObservable();
  isLoggedIn$: Observable<boolean> = this.user$.pipe(map(Boolean));


  constructor(private router: Router,private http:HttpClient) {
    // Al inicializar el servicio, verifica si hay un usuario en LocalStorage y cárgalo si es así.
    const usuarioString = localStorage.getItem('nombre');
    if (usuarioString) {
      this.nombre = JSON.parse(usuarioString);
      this.user.next(this.nombre);
    }
  }

  setUsuario(nuevoUsuario: string) {
    localStorage.setItem('usuario', JSON.stringify(nuevoUsuario));
    this.nombre = nuevoUsuario;
    this.user.next(nuevoUsuario);
  }

  eliminarUsuario() {
    localStorage.removeItem('usuario');
    this.nombre = null;
    this.user.next(null);
  }

  getUsuario(): string | null {
    return this.nombre;
  }

  isAuthenticated(): boolean {
    return !!this.getUsuario();
  }

}
