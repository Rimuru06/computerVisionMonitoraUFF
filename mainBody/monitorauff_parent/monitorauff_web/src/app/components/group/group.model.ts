import { BaseModel } from 'src/app/shared/base/base.model';
import { Monitor } from '../monitor/monitor.model';

export class Group extends BaseModel {
  parent_id!: number;
  name!: string;
  monitors!: Monitor[];

  constructor() {
    super();
  }
}
