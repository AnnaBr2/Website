import { copyFileSync, mkdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { join } from 'node:path';

const root = fileURLToPath(new URL('../', import.meta.url));
const destination = join(root, 'static/fonts');
mkdirSync(destination, { recursive: true });
for (const [family, weights] of [['montserrat', [400, 600, 700]]]) {
  const source = join(root, 'node_modules/@fontsource', family);
  for (const weight of weights) {
    const filename = `${family}-latin-${weight}-normal.woff2`;
    copyFileSync(join(source, 'files', filename), join(destination, filename));
  }
  copyFileSync(join(source, 'LICENSE'), join(destination, `${family}-LICENSE.txt`));
}
