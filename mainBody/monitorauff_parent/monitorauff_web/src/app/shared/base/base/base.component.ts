import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MessageService } from 'primeng/api';
import { DateUtils } from '../../utils/DateUtils';
import { BaseModel } from '../base.model';
import { BaseService } from '../base.service';

@Component({
  template: ` <p>base works!</p> `,
  styles: [],
})
export abstract class BaseComponent<T extends BaseModel> implements OnInit {
  constructor(
    protected service: BaseService<T>,
    protected route: ActivatedRoute,
    protected messageService: MessageService
  ) {}

  public abstract ngOnInit(): void;

  protected abstract afterLoadModel(): void;

  protected showSucessMessage(message?: string): void {
    let detail = message || 'Operação realizada com sucesso!';
    this.messageService.add({
      severity: 'success',
      summary: 'Success',
      detail: detail,
    });
  }

  protected showErrorMessage(message?: string): void {
    let detail = message || 'Não foi possível carregar os dados.';
    this.messageService.add({
      severity: 'error',
      summary: 'Erro',
      detail: detail,
    });
  }

  public dateToString(date: Date | undefined): string {
    if (!date) {
      return '';
    }
    return DateUtils.toFormattedDateTimeString(date);
  }
}
