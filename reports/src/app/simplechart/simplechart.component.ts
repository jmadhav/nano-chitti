import { Component, OnInit } from '@angular/core';
import { Chart } from 'angular-highcharts';
import { Http, Headers, RequestOptions, Response } from '@angular/http';
import { HttpClientModule } from '@angular/common/http';
import { Injectable } from '@angular/core';  
import { Observable, Subject } from 'rxjs/Rx';  
import 'rxjs/Rx'; //get everything from Rx    
import 'rxjs/add/operator/toPromise';  
import {Jsonp, JsonpModule } from '@angular/http';

@Injectable() 

@Component({
  selector: 'app-simplechart',
  templateUrl: './simplechart.component.html',
  styleUrls: ['./simplechart.component.css']
})

export class SimplechartComponent implements OnInit {

   data: any;
   chart: any;

   constructor(jsonp:Jsonp) {

    fetch('http://localhost:4200/assets/charts.json').then((response) => {
	    return response.json();
	  }).then((data) => {

		this.chart = new Chart({
		    chart: {
		      type: 'spline',
		      zoomType: 'x'
		    },
	        yAxis: {
		        title: {
		            text: 'Temperature (°C)'
		        }
		    },
		    xAxis: {
			        type: 'datetime' //ensures that xAxis is treated as datetime values
			    },
			 //     xAxis: {
    //     categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    // },
		    title: {
		      text: 'Linechart'
		    },
		    credits: {
		      enabled: false
		    },
		    series: data
		  });
		console.log(data);

	  }).catch((ex) => {
	    console.error('Error fetching users', ex);
	  });
  }

  ngOnInit() {
  	
  }
}