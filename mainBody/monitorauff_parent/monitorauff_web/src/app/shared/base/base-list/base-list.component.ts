import { Component } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { MessageService } from 'primeng/api';
import { BaseModel } from '../base.model';
import { BaseService } from '../base.service';
import { BaseComponent } from '../base/base.component';

@Component({
  template: `<p>base-list works!</p>`,
  styles: [],
})
export abstract class BaseListComponent<
  T extends BaseModel
> extends BaseComponent<T> {
  public modelList!: T[];

  constructor(
    service: BaseService<T>,
    protected router: Router,
    route: ActivatedRoute,
    messageService: MessageService
  ) {
    super(service, route, messageService);
  }

  ngOnInit(): void {
    this.loadModelList();
  }

  public loadModelList(): void {
    this.service.getAll().subscribe({
      next: (response: T[]) => {
        this.modelList = response;
        this.afterLoadModel();
      },
      error: (error: any) => {
        console.error(error);
        this.showErrorMessage();
      },
    });
  }

  public goToDetail(model: T): void {
    this.router.navigate([model.id], { relativeTo: this.route });
  }
}
