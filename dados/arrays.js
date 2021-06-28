let array_decrescente_1e3 = Array(10 ** 3);
for (let i = 0; i < 10 ** 3; i++) {
  array_decrescente_1e3[i] = (10 ** 3) - i - 1;
}

let array_decrescente_1e4 = Array(10 ** 4);
for (let i = 0; i < 10 ** 4; i++) {
  array_decrescente_1e4[i] = (10 ** 4) - i - 1;
}

let array_decrescente_1e5 = Array(10 ** 5);
for (let i = 0; i < 10 ** 5; i++) {
  array_decrescente_1e5[i] = (10 ** 5) - i - 1;
}

module.exports = {
  decrescente: {
    array_decrescente_1e3,
    array_decrescente_1e4,
    array_decrescente_1e5
  }
}