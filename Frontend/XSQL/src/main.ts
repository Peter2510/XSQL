import 'codemirror/mode/javascript/javascript';
import 'codemirror/mode/markdown/markdown';
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

import { AppModule } from './app/app.module';


platformBrowserDynamic().bootstrapModule(AppModule)
  .catch(err => console.error(err));
