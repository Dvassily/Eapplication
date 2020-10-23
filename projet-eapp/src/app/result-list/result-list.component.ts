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

  public fdata = JSON.parse("{\n" +
    "  \"query\": \"chat>artillerie\",\n" +
    "  \"definition\": {\n" +
    "    \"chat\": \"\",\n" +
    "    \"chat>mammif\u00e8re\": \"\",\n" +
    "    \"chat>communication textuelle\": \"\",\n" +
    "    \"chat>poisson\": \"\",\n" +
    "    \"chat>enrouement\": \"\",\n" +
    "    \"chat>machine de si\u00e8ge\": \"\",\n" +
    "    \"chat>f\u00e9lin\": \"\",\n" +
    "    \"chat>sexe de la femme\": \"\",\n" +
    "    \"chat>jeu\": \"\",\n" +
    "    \"chat>mammif\u00e8re>m\u00e2le\": \"\",\n" +
    "    \"chat>palatine\": \"\",\n" +
    "    \"chat>marine\": \"\",\n" +
    "    \"chat>artillerie\": \"\"\n" +
    "  },\n" +
    "  \"domainTerms\": [\n" +
    "    {\n" +
    "      \"nodeId\": 150,\n" +
    "      \"name\": \"'chat'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 5298,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 152397,\n" +
    "      \"name\": \"'Elevage'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 84,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 151850,\n" +
    "      \"name\": \"'Anatomie'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 292,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 151907,\n" +
    "      \"name\": \"'Biologie'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 306,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 152125,\n" +
    "      \"name\": \"'Zoologie'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 210,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 152578,\n" +
    "      \"name\": \"'V\u00e9t\u00e9rinaire'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 198,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 265176,\n" +
    "      \"name\": \"'ichthyologie'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 52,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 153082,\n" +
    "      \"name\": \"'Physiologie'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 124,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 267,\n" +
    "      \"name\": \"'Histoire'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 374,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 113902,\n" +
    "      \"name\": \"'alimentation'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 1622,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 175647,\n" +
    "      \"name\": \"'Ichthyologie'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 50,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 91657,\n" +
    "      \"name\": \"'nutrition'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 406,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 246797,\n" +
    "      \"name\": \"'biologie>246796'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 110,\n" +
    "      \"formattedName\": \"biologie>\u00e9tude du vivant\",\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 238798,\n" +
    "      \"name\": \"'esp\u00e8ce invasive'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 10,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 153845,\n" +
    "      \"name\": \"'Min\u00e9ralogie'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 112,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 143669,\n" +
    "      \"name\": \"'vert\u00e9br\u00e9s'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 80,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 162743,\n" +
    "      \"name\": \"'animaux de compagnie'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 110,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 155779,\n" +
    "      \"name\": \"'v\u00e9hicules'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 90,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 67368,\n" +
    "      \"name\": \"'m\u00e9canique'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 672,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 3674,\n" +
    "      \"name\": \"'botanique'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 1804,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 93056,\n" +
    "      \"name\": \"'enfance'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 796,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 36886,\n" +
    "      \"name\": \"'faune'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 398,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 135412,\n" +
    "      \"name\": \"'syst\u00e9matique'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 134,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 34460,\n" +
    "      \"name\": \"'synapsides'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 50,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 157132,\n" +
    "      \"name\": \"'f\u00e9lins'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 64,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 46164,\n" +
    "      \"name\": \"'carnivores'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 56,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 28663,\n" +
    "      \"name\": \"'min\u00e9ralogie'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 350,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 106404,\n" +
    "      \"name\": \"'ichtyologie'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 118,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 108750,\n" +
    "      \"name\": \"'poissons'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 400,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 195975,\n" +
    "      \"name\": \"'animaux domestiques'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 60,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 60361,\n" +
    "      \"name\": \"'loisirs'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 392,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 43729,\n" +
    "      \"name\": \"'m\u00e9decine v\u00e9t\u00e9rinaire'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 72,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 11567,\n" +
    "      \"name\": \"'taxonomie'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 128,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 341698,\n" +
    "      \"name\": \"'carnivore domestique'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 50,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 68883,\n" +
    "      \"name\": \"'agronomie'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 98,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 218905,\n" +
    "      \"name\": \"'faune>71539'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 22,\n" +
    "      \"formattedName\": \"faune>animaux\",\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 50567,\n" +
    "      \"name\": \"'agriculture'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 1784,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 116586,\n" +
    "      \"name\": \"'poliorc\u00e9tique'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 50,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 32851,\n" +
    "      \"name\": \"'mammif\u00e8res'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 144,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 68467,\n" +
    "      \"name\": \"'poisson'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 6785,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 138187,\n" +
    "      \"name\": \"'internet'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 2252,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 48855,\n" +
    "      \"name\": \"'carnivore'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 1530,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 143712,\n" +
    "      \"name\": \"'marine'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 1248,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 261439,\n" +
    "      \"name\": \"'armement m\u00e9di\u00e9val'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 50,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 2546,\n" +
    "      \"name\": \"'physiologie'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 334,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 146367,\n" +
    "      \"name\": \"'histoire'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 4162,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 123430,\n" +
    "      \"name\": \"'jeux'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 906,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 24742,\n" +
    "      \"name\": \"'cin\u00e9ma'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 6786,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 38710,\n" +
    "      \"name\": \"'litt\u00e9rature'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 3633,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 16033,\n" +
    "      \"name\": \"'cuisine'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 11094,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 18412,\n" +
    "      \"name\": \"'\u00e9levage'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 962,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 71539,\n" +
    "      \"name\": \"'animaux'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 1456,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 27154,\n" +
    "      \"name\": \"'animal domestique'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 402,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 53314,\n" +
    "      \"name\": \"'jeu'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 5070,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 76247,\n" +
    "      \"name\": \"'v\u00e9t\u00e9rinaire'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 590,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 35143,\n" +
    "      \"name\": \"'biologie'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 1904,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 117095,\n" +
    "      \"name\": \"'zoologie'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 1754,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 63235,\n" +
    "      \"name\": \"'mammif\u00e8re'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 3591,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 17559,\n" +
    "      \"name\": \"'animal'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 13751,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 39340,\n" +
    "      \"name\": \"'taxinomie'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 84,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 175720,\n" +
    "      \"name\": \"'Mammalia'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 50,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    },\n" +
    "    {\n" +
    "      \"nodeId\": 112609,\n" +
    "      \"name\": \"'anatomie'\",\n" +
    "      \"nodeType\": 1,\n" +
    "      \"weight\": 2908,\n" +
    "      \"formattedName\": null,\n" +
    "      \"isRefinement\": false\n" +
    "    }\n" +
    "  ]\n" +
    "}");

  constructor() { }

  ngOnInit(): void {
  }

  onClickDef(item) {
    this.selectItem.emit(item);
  }

}
