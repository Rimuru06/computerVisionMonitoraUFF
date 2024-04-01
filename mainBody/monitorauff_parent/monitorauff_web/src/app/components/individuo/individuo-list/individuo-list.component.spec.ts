import { ComponentFixture, TestBed } from '@angular/core/testing';

import { IndividuoListComponent } from './individuo-list.component';

describe('IndividuoComponent', () => {
  let component: IndividuoListComponent;
  let fixture: ComponentFixture<IndividuoListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [IndividuoListComponent],
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(IndividuoListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
