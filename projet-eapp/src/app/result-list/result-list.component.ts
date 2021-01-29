import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {ServerService} from '../services/server.service';

@Component({
  selector: 'app-result-list',
  templateUrl: './result-list.component.html',
  styleUrls: ['./result-list.component.css']
})
export class ResultListComponent implements OnInit {


  @Input()
  public data;

  @Output() selectItem: EventEmitter<any> = new EventEmitter();


  public defMap = {
    DEFINITIONS_KEY: 'definitions',
    DOMAIN_TERMS_KEY: 'domainTerms',
    ASSOCIATIONS_KEY: 'associations',
    PARTS_KEY: 'parts',
  };

  constructor(private serverService: ServerService) { }

  ngOnInit(): void {
  }

  onClickDef(item) {
    this.selectItem.emit(item);
  }


  loadDefinitions() {
    this.serverService.getResult(':GET \'' + this.data.query.term + '\' :DEFINITIONS').subscribe(res => {
      this.data = res;
    });
  }

  mustDisplayCategories() {
    return (this.data.query.properties.length !== 1);
  }

  getDefinitions() {
    const result = [];
    const regexp = new RegExp(/\s*([1-9]\s*\.)/gm);


    return this.data.definitions.join(' ');
  }
}
