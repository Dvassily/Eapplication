import { Component, OnInit, EventEmitter, Output } from '@angular/core';
import { FormBuilder, FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css']
})
export class SearchBarComponent implements OnInit {

  @Output() onSearch = new EventEmitter<any>();

  constructor(private formBuilder : FormBuilder) { }

  ngOnInit(): void {

  }

  submitQuery(input: string): void {
    let query = '';
    let tokens = input.trim().split(' ');
    let resultTokens = []

    // for (let index in tokens) {
    //   if (! tokens[index].startsWith(':')) {
    //     resultTokens.push('\'' + tokens[index] + '\'');
    //   } else {
    //     resultTokens.push(tokens[index]);
    //   }
    // }

    this.onSearch.emit(input);
  }

  onValueChanged(input): void {
    this.submitQuery(input.target.value);
  }
}
