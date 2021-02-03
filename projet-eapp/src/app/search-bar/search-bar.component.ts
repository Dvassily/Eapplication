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
  mot : string;

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

  formatLabel(value: number) {

    return `${Math.floor((value * 100) / 30000)}%`;
  }


  onValueChanged(input): void {
    this.mot = input.target.value;
    this.submitQuery(input.target.value);
  }
  getValue(){
    return this.mot;
  }
}
