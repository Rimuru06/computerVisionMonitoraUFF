import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardLayoutComponent } from './components/dashboard-layout/dashboard-layout.component';
import { EtiquetaIndividuoDetailComponent } from './components/etiqueta-individuo/etiqueta-individuo-detail/etiqueta-individuo-detail.component';
import { EtiquetaIndividuoListComponent } from './components/etiqueta-individuo/etiqueta-individuo-list/etiqueta-individuo-list.component';
import { HomeComponent } from './components/home/home.component';
import { IndividuoDetailComponent } from './components/individuo/individuo-detail/individuo-detail.component';
import { IndividuoListComponent } from './components/individuo/individuo-list/individuo-list.component';
import { MonitorDetailComponent } from './components/monitor/monitor-detail/monitor-detail.component';
import { MonitorListComponent } from './components/monitor/monitor-list/monitor-list.component';
import { NotFoundComponent } from './components/not-found/not-found.component';
import { OcorrenciaFaceDetailComponent } from './components/ocorrencia-face/ocorrencia-face-detail/ocorrencia-face-detail.component';
import { OcorrenciaFaceListComponent } from './components/ocorrencia-face/ocorrencia-face-list/ocorrencia-face-list.component';
import { PermissaoIndividuoDetailComponent } from './components/permissao-individuo/permissao-individuo-detail/permissao-individuo-detail.component';
import { PermissaoIndividuoListComponent } from './components/permissao-individuo/permissao-individuo-list/permissao-individuo-list.component';
import { ServicoDeteccaoFaceDetailComponent } from './components/servicos/deteccao-face/servico-deteccao-face-detail/servico-deteccao-face-detail.component';
import { ServicoDeteccaoFaceListComponent } from './components/servicos/deteccao-face/servico-deteccao-face-list/servico-deteccao-face-list.component';
import { TipoServicoDetailComponent } from './components/servicos/tipo-servico/tipo-servico-detail/tipo-servico-detail.component';
import { TipoServicoListComponent } from './components/servicos/tipo-servico/tipo-servico-list/tipo-servico-list.component';
import { WelcomeComponent } from './components/welcome/welcome.component';

const routes: Routes = [
  {
    path: '',
    component: WelcomeComponent,
  },
  {
    path: '',
    component: DashboardLayoutComponent,
    children: [
      { path: 'home', component: HomeComponent },
      { path: 'face', component: OcorrenciaFaceListComponent },
      { path: 'face/:id', component: OcorrenciaFaceDetailComponent },
      { path: 'individuo', component: IndividuoListComponent },
      { path: 'individuo/:id', component: IndividuoDetailComponent },
      { path: 'etiqueta-individuo', component: EtiquetaIndividuoListComponent },
      {
        path: 'etiqueta-individuo/:id',
        component: EtiquetaIndividuoDetailComponent,
      },
      {
        path: 'permissao-individuo',
        component: PermissaoIndividuoListComponent,
      },
      {
        path: 'permissao-individuo/:id',
        component: PermissaoIndividuoDetailComponent,
      },
      { path: 'monitor', component: MonitorListComponent },
      { path: 'monitor/:id', component: MonitorDetailComponent },
      { path: 'tipo-servico', component: TipoServicoListComponent },
      { path: 'tipo-servico/:id', component: TipoServicoDetailComponent },
      { path: 'deteccao-face', component: ServicoDeteccaoFaceListComponent },
      {
        path: 'deteccao-face/:id',
        component: ServicoDeteccaoFaceDetailComponent,
      },
    ],
  },
  { path: '', redirectTo: '/', pathMatch: 'full' },
  { path: '**', component: NotFoundComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
