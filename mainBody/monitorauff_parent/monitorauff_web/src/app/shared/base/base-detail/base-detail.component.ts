import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MessageService } from 'primeng/api';
import { BaseModel } from '../base.model';
import { BaseService } from '../base.service';
import { BaseComponent } from '../base/base.component';

@Component({
  template: `<p>base-detail works!</p>`,
  styles: [],
})
export abstract class BaseDetailComponent<
  T extends BaseModel
> extends BaseComponent<T> {
  public model!: T;

  constructor(
    service: BaseService<T>,
    route: ActivatedRoute,
    messageService: MessageService
  ) {
    super(service, route, messageService);
  }

  ngOnInit(): void {
    let modelId: number = this.route.snapshot.params['id'];
    this.loadModel(modelId);
  }

  protected loadModel(id: number): void {
    this.service.get(id).subscribe({
      next: (response: T) => {
        this.model = response;
        this.afterLoadModel();
      },
      error: (error: any) => {
        console.error(error);
        this.showErrorMessage();
      },
    });
  }
}
