import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OcorrenciaFaceListComponent } from './ocorrencia-face-list.component';

describe('OcorrenciaFaceListComponent', () => {
  let component: OcorrenciaFaceListComponent;
  let fixture: ComponentFixture<OcorrenciaFaceListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OcorrenciaFaceListComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OcorrenciaFaceListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
