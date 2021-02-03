import { Component, OnInit, EventEmitter, Output } from '@angular/core';
import { FormBuilder, FormGroup, FormControl } from '@angular/forms';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css']
})
export class SearchBarComponent implements OnInit {

  @Output() onSearch = new EventEmitter<any>();


  public model = '';
  
  constructor(private formBuilder : FormBuilder,   private route: ActivatedRoute,
    ) { }

  ngOnInit(): void {

    this.route.queryParams.subscribe(params => {

      console.log("test called")
      if(params['search']) {
        this.model = params['search'];
        this.submitQuery()
      }
    });
  
  }

  submitQuery(): void {
    this.onSearch.emit(this.model);
  }

  formatLabel(value: number) {

    return `${Math.floor((value * 100) / 30000)}%`;
  }


}
