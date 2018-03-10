
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { ChartModule } from 'angular-highcharts';

import { SimplechartComponent } from './simplechart.component';

@NgModule({
  imports: [
    CommonModule,
    RouterModule,
    FormsModule,
    ChartModule
  ],
  declarations: [
    SimplechartComponent
  ],
  exports: [
    SimplechartComponent
  ]
})
export class SimplechartModule { }
