import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ObtencionDBdumpComponent } from './obtencion-dbdump.component';

describe('ObtencionDBdumpComponent', () => {
  let component: ObtencionDBdumpComponent;
  let fixture: ComponentFixture<ObtencionDBdumpComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ObtencionDBdumpComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ObtencionDBdumpComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
