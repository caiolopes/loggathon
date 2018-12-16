import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable()
export class RoutingProvider {

  URL_PATH = "http://10.0.30.118:5000/make_route";

  constructor(public http: HttpClient) {
    
  }

  getRoute() {
    return this.http.get("http://10.0.30.118:5000/make_route");
  }

}
