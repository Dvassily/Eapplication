import {AfterViewInit, Component, Input, OnInit} from '@angular/core';
import {MatSlider} from "@angular/material/slider";

@Component({
  selector: 'app-word-detail',
  templateUrl: './word-detail.component.html',
  styleUrls: ['./word-detail.component.css']
})
export class WordDetailComponent implements OnInit {


  @Input() title: string;
  @Input() terms: Array<any>;

  public domainTermsWeight;

  constructor() {
  }

  ngOnInit(): void {
    this.domainTermsWeight = 0;
  }


  formatLabel(value: number) {
    return `${Math.floor((value * 100)  / (this as unknown)['max'])}%`;
  }

  name(term : object) : string {
    if (term['formattedName'] !== null) {
      return term['formattedName'];
    }

    return term['name'];
  }

  get getTermMaxWeight() {

    const res = this.terms.reduce((acc, newValue) => {
      if (newValue > acc) {
        acc = newValue;
      }
    }, 0);

    return res;
  }
}
