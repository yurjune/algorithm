// 소인수분해: 어떤 수를 소수들의 곱으로 표현하는 것

function factorization(N) {
  const result = [];
  let divisor = 2;

  while (N >= 2) {
    if (N % divisor === 0) {
      N /= divisor;
      result.push(divisor);
      continue;
    }

    divisor++;
  }

  return result;
}
