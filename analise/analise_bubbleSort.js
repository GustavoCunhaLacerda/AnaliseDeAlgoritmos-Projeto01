const fs = require('fs');
const { performance } = require('perf_hooks');

const { decrescente } = require('../dados/arrays');
const { bubbleSort } = require('../algoritmos/bubbleSort')

function piorCaso() {
  let pior_caso = {
    tempo: {
      '1e3': [],
      '1e4': [],
      '1e5': []
    },
    espaco: {
      '1e3': [],
      '1e4': [],
      '1e5': []
    }
  }
  let antes;
  for (let index = 0; index < 20; index++) {
    antes = performance.now()
    bubbleSort([...decrescente.array_decrescente_1e3]);
    pior_caso.tempo['1e3'].push(performance.now() - antes);

    antes = performance.now()
    bubbleSort([...decrescente.array_decrescente_1e4]);
    pior_caso.tempo['1e4'].push(performance.now() - antes);

    antes = performance.now()
    bubbleSort([...decrescente.array_decrescente_1e5]);
    pior_caso.tempo['1e5'].push(performance.now() - antes);
  }

  console.log(pior_caso);
  const data = JSON.stringify(pior_caso);

  fs.writeFile('PiorCaso.json', data, (err) => {
    if (err) { throw err }
    console.log("Dados do pior caso armazenados.");
  });
}

piorCaso();