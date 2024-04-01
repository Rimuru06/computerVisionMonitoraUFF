import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ServicoDeteccaoFaceListComponent } from './servico-deteccao-face-list.component';

describe('ServicoDeteccaoFaceListComponent', () => {
  let component: ServicoDeteccaoFaceListComponent;
  let fixture: ComponentFixture<ServicoDeteccaoFaceListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ServicoDeteccaoFaceListComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ServicoDeteccaoFaceListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
