import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';

@Component({
  selector: 'app-result-list',
  templateUrl: './result-list.component.html',
  styleUrls: ['./result-list.component.css']
})
export class ResultListComponent implements OnInit {


  @Input()
  public data;

  @Output() selectItem: EventEmitter<any> = new EventEmitter();

  constructor() { }

  ngOnInit(): void {
  }

  onClickDef(item) {
    this.selectItem.emit(item);
  }

  mustDisplayCategories() {
    return (this.data.query.properties.length !== 1);
  }

  definitions() {
    let result = []

    for (let definition of this.data.definitions) {
      console.log(definition);
      const regexp = new RegExp("/\d\.\s/g");
      let subDefinitions = definition.split(regexp)
      console.log(subDefinitions);
      result.push(definition);
    }

    return result;
  }
}
