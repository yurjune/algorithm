/**
 * 최대공약수(GCD): 두 수의 공통된 약수 중 가장 큰 약수
 * 최소공배수(LCM): 두 수의 공통인 배수 중 가장 작은 수
 *
 * - 최대공약수 구하기
 * 유클리드 호제법으로 구한다.
 *
 * - 최소공배수 구하기
 * 최소공배수 = (num1 * num2) / GCD(num1, num2)
 *
 * - 유클리드 호제법
 * num1를 num2로 나눈 나머지가 r일때, GCD(num1, num2) = GCD(num2, r) 이다.
 * 이 때, r이 0이면 num2가 num1과 num2의 최대공약수가 된다.
 */

const gcd = (n, m) => (m ? gcd(m, n % m) : n);
const lcm = (n, m) => (n * m) / gcd(n, m);

console.log(gcd(12, 24)); // 12
console.log(lcm(12, 24)); // 24
