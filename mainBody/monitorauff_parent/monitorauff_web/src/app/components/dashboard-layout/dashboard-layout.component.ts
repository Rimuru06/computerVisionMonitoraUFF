import { Component, OnInit } from '@angular/core';
import { MenuItem } from 'primeng/api';

@Component({
  selector: 'app-dashboard-layout',
  templateUrl: './dashboard-layout.component.html',
  styleUrls: ['./dashboard-layout.component.scss'],
})
export class DashboardLayoutComponent implements OnInit {
  constructor() {}

  items: MenuItem[] = [];

  ngOnInit(): void {
    this.items = [
      { label: 'Início', routerLink: ['/home'] },
      { label: 'Faces', routerLink: ['/face'] },
      { label: 'Indivíduos', routerLink: ['/individuo'] },
      { label: 'Etiquetas', routerLink: ['/etiqueta-individuo'] },
      { label: 'Permissões', routerLink: ['/permissao-individuo'] },
      { label: 'Monitores', routerLink: ['/monitor'] },
    ];
  }
}
