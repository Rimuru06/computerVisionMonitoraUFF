import { BaseModel } from 'src/app/shared/base/base.model';

export class OcorrenciaFace extends BaseModel {
  public individuo!: number;
  public camera_id!: number;
  public img_filename!: string;
  public data_md5!: string;

  constructor() {
    super();
  }
}
