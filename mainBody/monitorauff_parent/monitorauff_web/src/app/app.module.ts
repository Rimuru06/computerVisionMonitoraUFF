import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';

import { AvatarModule } from 'primeng/avatar';
import { ButtonModule } from 'primeng/button';
import { BadgeModule } from 'primeng/badge';
import { CardModule } from 'primeng/card';
import { ChipModule } from 'primeng/chip';
import { DividerModule } from 'primeng/divider';
import { DropdownModule } from 'primeng/dropdown';
import { FileUploadModule } from 'primeng/fileupload';
import { ImageModule } from 'primeng/image';
import { MenuModule } from 'primeng/menu';
import { MessageModule } from 'primeng/message';
import { MessagesModule } from 'primeng/messages';
import { MultiSelectModule } from 'primeng/multiselect';
import { SidebarModule } from 'primeng/sidebar';
import { SkeletonModule } from 'primeng/skeleton';
import { TableModule } from 'primeng/table';

import { DashboardLayoutComponent } from './components/dashboard-layout/dashboard-layout.component';
import { HomeComponent } from './components/home/home.component';
import { IndividuoListComponent } from './components/individuo/individuo-list/individuo-list.component';
import { NotFoundComponent } from './components/not-found/not-found.component';
import { WelcomeComponent } from './components/welcome/welcome.component';
import { IndividuoDetailComponent } from './components/individuo/individuo-detail/individuo-detail.component';
import { OcorrenciaFaceListComponent } from './components/ocorrencia-face/ocorrencia-face-list/ocorrencia-face-list.component';
import { OcorrenciaFaceDetailComponent } from './components/ocorrencia-face/ocorrencia-face-detail/ocorrencia-face-detail.component';
import { MessageService } from 'primeng/api';
import { EtiquetaIndividuoListComponent } from './components/etiqueta-individuo/etiqueta-individuo-list/etiqueta-individuo-list.component';
import { EtiquetaIndividuoDetailComponent } from './components/etiqueta-individuo/etiqueta-individuo-detail/etiqueta-individuo-detail.component';
import { PermissaoIndividuoListComponent } from './components/permissao-individuo/permissao-individuo-list/permissao-individuo-list.component';
import { PermissaoIndividuoDetailComponent } from './components/permissao-individuo/permissao-individuo-detail/permissao-individuo-detail.component';
import { MonitorListComponent } from './components/monitor/monitor-list/monitor-list.component';
import { MonitorDetailComponent } from './components/monitor/monitor-detail/monitor-detail.component';
import { GroupListComponent } from './components/group/group-list/group-list.component';
import { GroupDetailComponent } from './components/group/group-detail/group-detail.component';
import { ServicoDeteccaoFaceListComponent } from './components/servicos/deteccao-face/servico-deteccao-face-list/servico-deteccao-face-list.component';
import { ServicoDeteccaoFaceDetailComponent } from './components/servicos/deteccao-face/servico-deteccao-face-detail/servico-deteccao-face-detail.component';
import { TipoServicoDetailComponent } from './components/servicos/tipo-servico/tipo-servico-detail/tipo-servico-detail.component';
import { TipoServicoListComponent } from './components/servicos/tipo-servico/tipo-servico-list/tipo-servico-list.component';

@NgModule({
  declarations: [
    AppComponent,
    DashboardLayoutComponent,
    HomeComponent,
    IndividuoDetailComponent,
    IndividuoListComponent,
    OcorrenciaFaceListComponent,
    OcorrenciaFaceDetailComponent,
    NotFoundComponent,
    WelcomeComponent,
    EtiquetaIndividuoListComponent,
    EtiquetaIndividuoDetailComponent,
    PermissaoIndividuoListComponent,
    PermissaoIndividuoDetailComponent,
    MonitorListComponent,
    MonitorDetailComponent,
    GroupListComponent,
    GroupDetailComponent,
    ServicoDeteccaoFaceListComponent,
    ServicoDeteccaoFaceDetailComponent,
    TipoServicoDetailComponent,
    TipoServicoListComponent,
  ],
  imports: [
    AppRoutingModule,
    AvatarModule,
    BadgeModule,
    BrowserAnimationsModule,
    BrowserModule,
    ButtonModule,
    CardModule,
    ChipModule,
    DividerModule,
    DropdownModule,
    FileUploadModule,
    FormsModule,
    HttpClientModule,
    ImageModule,
    MenuModule,
    MessageModule,
    MessagesModule,
    MultiSelectModule,
    SidebarModule,
    SkeletonModule,
    TableModule,
  ],
  providers: [MessageService],
  bootstrap: [AppComponent],
})
export class AppModule {}
