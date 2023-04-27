/**
 * 에라토스테네스의 체
 * - 2부터 N 범위의 소수를 구하기
 * - 소수의 배수는 소수가 아님을 이용하여 모두 소거
 *
 * - 방법
 * 2부터 N까지 구간에 대하여:
 * 2는 소수이므로 2의 배수들 중 남아있는 수들을 모두 지운다.
 * 남아있는 수 가운데 3은 소수이므로 3의 배수들을 모두 지운다.
 * 이 과정을 반복한다.
 */

const primesUpToN = (N) => {
  const primes = [false, false, ...Array(N - 1).fill(true)];

  for (let i = 2; i <= N; i++) {
    if (!primes[i]) continue;

    for (let j = 2; i * j <= N; j++) {
      primes[i * j] = false;
    }
  }

  return primes.reduce((acc, cur, idx) => {
    if (cur) acc.push(idx);
    return acc;
  }, []);
};

console.log(primesUpToN(20)); // [2, 3, 5, 7, 11, 13, 17, 19]
