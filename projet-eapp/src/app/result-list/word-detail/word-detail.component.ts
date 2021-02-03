import {AfterViewInit, Component, Input, OnInit} from '@angular/core';
import {MatSlider} from "@angular/material/slider";
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-word-detail',
  templateUrl: './word-detail.component.html',
  styleUrls: ['./word-detail.component.css']
})
export class WordDetailComponent implements OnInit {

  @Input() title: string;
  @Input() terms: Array<any>;

  public domainTermsWeight;
  public model = '';
  public fileteredWords: Array<any>;

  constructor(private route: ActivatedRoute, private router: Router) {
  }

  ngOnInit(): void {
    this.domainTermsWeight = 300;
    this.fileteredWords = this.terms;
  }

  search(term: string): void {
    if(!term || term.length <= 0)
      this.fileteredWords = this.terms;
    
    this.fileteredWords = this.terms.filter((value, idx) => {
      return value.name.search(term.toLocaleLowerCase()) != -1;
    });
  }

  formatLabel(value: number) {
    return `${Math.floor((value * 100)  / (this as unknown)['max'])}%`;
  }

  onSearchWord(term) {
    this.router.navigateByUrl(`/?search=${term.name}`)
  }


   getTermMaxWeight() {

    let max = 0;
  
    for(let term of this.terms) {
        console.log(term)
    }

    return 0;
  }

  name(term : object) : string {
    if (term['formattedName'] !== null) {
      return term['formattedName'];
    }

    return term['name'];
  }

  getTermColor(term){
    if( term.weight >= 80 ){
      return 'first';
    } else{ 
        if( term.weight >= 60 && term.weight <= 80 ){
         return 'second';
      } else{
          if( term.weight >= 40 && term.weight < 60 ){
            return 'third';
          } else return 'fourth';
      } 
    } 
  }
}
