/**
 * N의 약수를 구할 때, N의 제곱근까지의 약수만 계산하면 된다.
 * 약수끼리의 곱은 N의 제곱근을 기준으로 대칭으로 이루어져있다.
 *
 * 약수 구하기:
 * 1. 1부터 N의 제곱근까지의 수 중 N과 나누어 나머지가 0인 수
 * 2. 1번에서 구한 수를 N과 나눈 수 (단, 중복 제거 필요)
 */

const getDivisors = (num) => {
  const arr = [];
  sqrt = Math.floor(Math.sqrt(num));

  for (let i = 1; i <= sqrt; i++) {
    if (num % i == 0) {
      arr.push(i);
      if (i !== num / i) arr.push(num / i);
    }
  }

  return arr;
};

const result = getDivisors(100).sort((a, b) => a - b);
console.log(result);

// 성능 최적화x
const getDivisors2 = (num) =>
  Array(num)
    .fill()
    .map((_, i) => i + 1)
    .filter((v) => num % v == 0);
