let star = '';
const size = 10;

for (let i = 0; i < size; i++) {
  for (let j = size - 1; j > i; j--) {
    star += ' ';
  }
  for (let k = 0; k < 2 * i + 1; k++) {
    star += '*';
  }
  star += '\n';
}

for (let i = size - 1; i > 0; i--) {
  for (let j = size; j > i; j--) {
    star += ' ';
  }
  for (let k = 0; k < 2 * i - 1; k++) {
    star += '*';
  }
  star += '\n';
}

console.log(star);
