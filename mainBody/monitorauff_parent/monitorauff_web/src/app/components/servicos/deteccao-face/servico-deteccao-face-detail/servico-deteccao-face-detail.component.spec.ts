import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ServicoDeteccaoFaceDetailComponent } from './servico-deteccao-face-detail.component';

describe('ServicoDeteccaoFaceDetailComponent', () => {
  let component: ServicoDeteccaoFaceDetailComponent;
  let fixture: ComponentFixture<ServicoDeteccaoFaceDetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ServicoDeteccaoFaceDetailComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ServicoDeteccaoFaceDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
