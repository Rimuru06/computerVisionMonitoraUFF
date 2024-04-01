import { Component, ViewChild } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { MessageService } from 'primeng/api';
import { FileUpload } from 'primeng/fileupload';
import { BaseListComponent } from 'src/app/shared/base/base-list/base-list.component';
import { EtiquetaIndividuo } from '../../etiqueta-individuo/etiqueta-individuo.model';
import { EtiquetaIndividuoService } from '../../etiqueta-individuo/etiqueta-individuo.service';
import { Individuo } from '../individuo.model';
import { IndividuoService } from '../individuo.service';

@Component({
  selector: 'app-individuo-list',
  templateUrl: './individuo-list.component.html',
  styleUrls: ['./individuo-list.component.scss'],
})
export class IndividuoListComponent extends BaseListComponent<Individuo> {
  @ViewChild('fileUploader') fileUploader!: FileUpload;

  public filtered: boolean = false;
  public etiquetas: EtiquetaIndividuo[] = [];

  constructor(
    override service: IndividuoService,
    router: Router,
    route: ActivatedRoute,
    messageService: MessageService,
    private etiquetaService: EtiquetaIndividuoService
  ) {
    super(service, router, route, messageService);
  }

  protected afterLoadModel(): void {
    this.modelList.forEach((individuo) => {
      if (!individuo.etiquetas || individuo.etiquetas.length == 0) return;

      individuo.etiquetas.forEach((etiquetaId) => {
        this.etiquetaService.get(etiquetaId).subscribe({
          next: (response) => {
            if (!this.etiquetas.some((e) => e.id === etiquetaId)) {
              this.etiquetas.push(response);
            }
          },
          error: (error: any) => {
            let msg = `Não foi possível carregar a etiqueta de ID ${etiquetaId}`;
            this.showErrorMessage();
          },
        });
      });
    });
  }

  public onFiltering($event: any): void {
    this.service.filterByImage($event.files[0]).subscribe({
      next: (response: Individuo[]) => {
        this.modelList = response;
        this.filtered = true;
        this.fileUploader.clear();
        this.afterLoadModel();
      },
      error: (error: any) => {
        console.error(error);
        this.showErrorMessage();
      },
    });
  }

  public clearFilter(): void {
    this.loadModelList();
    this.filtered = false;
  }

  public getEtiqueta(id: number): EtiquetaIndividuo | null {
    if (!id) return null;

    let etiqueta = this.etiquetas.find((i) => i.id === id);

    return etiqueta || null;
  }

  public getEtiquetas(individuo: Individuo): EtiquetaIndividuo[] {
    let etiquetas: EtiquetaIndividuo[] = [];

    individuo.etiquetas.forEach((e) => {
      let etiqueta = this.getEtiqueta(e);

      if (etiqueta) etiquetas.push(etiqueta);
    });

    return etiquetas;
  }
}
