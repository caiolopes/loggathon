import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';


@IonicPage()
@Component({
  selector: 'page-items',
  templateUrl: 'items.html',
})
export class ItemsPage {

  url = "http://10.0.30.118:5000/static/media/"

  items = this.navParams.data;

  constructor(public navCtrl: NavController, public navParams: NavParams) {
    this.items.forEach(el => {
      el.image = this.url + el.image;
    });
  }


}
