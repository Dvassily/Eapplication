import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";


@Injectable()
export class ServerService {
  constructor(private httpClient: HttpClient) {
  }

  getResult(query, noCache = false) {

    let reqUrl = `http://localhost:5000/get/${query}`;

    if(noCache) {
      reqUrl += '?disabled_cache=true';
    }

    return this.httpClient.get(reqUrl)
  }

  parseRequest(query) {
    return this.httpClient.get(`http://localhost:5000/parse_query/${query}`)
  }
}
