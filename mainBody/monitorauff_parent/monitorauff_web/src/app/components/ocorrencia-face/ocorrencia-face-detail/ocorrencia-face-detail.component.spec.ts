import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OcorrenciaFaceDetailComponent } from './ocorrencia-face-detail.component';

describe('OcorrenciaFaceDetailComponent', () => {
  let component: OcorrenciaFaceDetailComponent;
  let fixture: ComponentFixture<OcorrenciaFaceDetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OcorrenciaFaceDetailComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OcorrenciaFaceDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
