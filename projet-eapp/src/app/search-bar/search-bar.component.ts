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

    this.searchForm.get('searchFormInput')
      .valueChanges.subscribe(this.onValueChanged);
  }

  submitQuery(): void {
    let query = '';
    let tokens = this.searchForm.value.searchFormInput.split(' ');
    let resultTokens = []

    for (let index in tokens) {
      if (! tokens[index].startsWith(':')) {
        resultTokens.push('\'' + tokens[index] + '\'');
      } else {
        resultTokens.push(tokens[index]);
      }
    }

    this.querySubmitted.emit(resultTokens.join(' '));
  }

  onValueChanged(input): void {
    setTimeout(function() {

    }, 350);
  }
}
