import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MessageService } from 'primeng/api';
import { BaseDetailComponent } from 'src/app/shared/base/base-detail/base-detail.component';
import { ServicoDeteccaoFace } from '../../servicos/deteccao-face/servico-deteccao-face.model';
import { ServicoDeteccaoFaceService } from '../../servicos/deteccao-face/servico-deteccao-face.service';
import { TipoServico } from '../../servicos/tipo-servico/tipo-servico.model';
import { TipoServicoService } from '../../servicos/tipo-servico/tipo-servico.service';
import { TipoServicoEnum } from '../../servicos/tipo-servico/tipo-serviço.enum';
import { Monitor } from '../monitor.model';
import { MonitorService } from '../monitor.service';

@Component({
  selector: 'app-monitor-detail',
  templateUrl: './monitor-detail.component.html',
  styleUrls: ['./monitor-detail.component.scss'],
})
export class MonitorDetailComponent extends BaseDetailComponent<Monitor> {
  public tiposServico: TipoServico[] = [];
  public tipoServicoOptions: TipoServico[] = [];
  public selectedTipoServico: TipoServico[] = [];
  public TipoServicoEnum = TipoServicoEnum;

  private readonly servicos: any = {
    2: {
      ativar: () => this.ativarServicoDeteccaoFace(),
      desativar: () => this.desativarServicoDeteccaoFace(),
      isActivated: false,
    },
  };

  constructor(
    override service: MonitorService,
    route: ActivatedRoute,
    messageService: MessageService,
    private deteccaoFaceService: ServicoDeteccaoFaceService,
    private tipoServicoService: TipoServicoService
  ) {
    super(service, route, messageService);
  }

  override ngOnInit(): void {
    super.ngOnInit();
    this.loadOptions();
  }

  protected afterLoadModel(): void {
    this.tipoServicoService.getByMonitorId(this.model.id).subscribe({
      next: (response: TipoServico[]) => {
        this.tiposServico = response;

        this.servicos[2].isActivated = false;

        this.deteccaoFaceService.getAll({ monitor: this.model.id }).subscribe({
          next: (response) => {
            if (response.length) {
              this.servicos[2].isActivated = true;
            }
          },
          error: (error: any) => {
            let msg = `Não foi possível verificar ativação do serviço de face`;
            this.showErrorMessage(msg);
          },
        });
      },
      error: (error: any) => {
        let msg = `Não foi possível carregar os serviços desse monitor`;
        this.showErrorMessage(msg);
      },
    });
  }

  private loadOptions(): void {
    this.tipoServicoService.getAll().subscribe({
      next: (response: TipoServico[]) => {
        this.tipoServicoOptions = response;
      },
      error: (error: any) => {
        console.error(error);
        this.showErrorMessage('Erro ao carregar opções de tipos de serviço.');
      },
    });
  }

  public estaAtivado(tipo: TipoServico): boolean {
    return this.servicos[tipo.id]?.isActivated || false;
  }

  public servicoExiste(tipo: TipoServico): boolean {
    return this.servicos[tipo.id] ? true : false;
  }

  public ativarServico(tipo: TipoServico): void {
    this.servicos[tipo.id].ativar();
  }

  public desativarServico(tipo: TipoServico): void {
    this.servicos[tipo.id].desativar();
  }

  private ativarServicoDeteccaoFace(): void {
    if (!this.model) return;

    this.deteccaoFaceService.ativarServico(this.model.id).subscribe({
      next: () => {
        this.showSucessMessage(
          'Servico de detecção de face ativado com sucesso'
        );
        this.loadModel(this.model.id);
        this.selectedTipoServico = [];
      },
      error: () => {
        this.showErrorMessage('Não foi possível realizar a operação.');
        this.selectedTipoServico = [];
      },
    });
  }

  private desativarServicoDeteccaoFace(): void {
    if (!this.model) return;

    this.deteccaoFaceService.desativarServico(this.model.id).subscribe({
      next: () => {
        this.showSucessMessage(
          'Servico de detecção de face desativado com sucesso'
        );
        this.loadModel(this.model.id);
        this.selectedTipoServico = [];
      },
      error: () => {
        this.showErrorMessage('Não foi possível realizar a operação.');
        this.selectedTipoServico = [];
      },
    });
  }

  public vincularTipoServico(): void {
    this.selectedTipoServico.forEach((tipo) => {
      this.tipoServicoService
        .vincularMonitor(tipo.id, [this.model.id])
        .subscribe({
          next: () => {
            this.showSucessMessage();
            this.loadModel(this.model.id);
            this.selectedTipoServico = [];
          },
          error: () => {
            this.showErrorMessage('Não foi possível realizar a operação.');
            this.selectedTipoServico = [];
          },
        });
    });
  }

  public desvincularTipoServico(tipo: TipoServico): void {
    this.tipoServicoService
      .desvincularMonitor(tipo.id, [this.model.id])
      .subscribe({
        next: () => {
          this.showSucessMessage();
          this.loadModel(this.model.id);
        },
        error: () => {
          this.showErrorMessage('Não foi possível realizar a operação.');
        },
      });
  }
}
