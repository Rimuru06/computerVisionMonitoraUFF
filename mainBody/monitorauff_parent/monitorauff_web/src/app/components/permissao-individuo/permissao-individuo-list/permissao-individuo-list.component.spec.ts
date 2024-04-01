import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PermissaoIndividuoListComponent } from './permissao-individuo-list.component';

describe('PermissaoIndividuoListComponent', () => {
  let component: PermissaoIndividuoListComponent;
  let fixture: ComponentFixture<PermissaoIndividuoListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PermissaoIndividuoListComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PermissaoIndividuoListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
