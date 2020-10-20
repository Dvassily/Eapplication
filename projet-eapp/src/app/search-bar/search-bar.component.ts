import { Component, OnInit, EventEmitter, Output } from '@angular/core';
import { FormBuilder, FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css']
})
export class SearchBarComponent implements OnInit {
  searchForm: FormGroup;
  @Output() querySubmitted = new EventEmitter<any>();
  
  constructor(private formBuilder : FormBuilder) { }

  ngOnInit(): void {
    this.searchForm = new FormGroup({
      searchFormInput: new FormControl('')
    });
  }

  submitQuery(): void {
    this.querySubmitted.emit(this.searchForm.value.searchFormInput);
  }
}
