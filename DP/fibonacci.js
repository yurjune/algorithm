// F0 = 0, F1 = 1, Fn = Fn-1 + Fn-2

// 재귀, top-down
function fib(n, memo) {
  if (n < 2) return n;
  if (memo[n]) return memo[n];

  return (memo[n] = fib(n - 1, memo) + fib(n - 2, memo));
}

// 반복문, bottom-up
function fibo(n) {
  const memo = [0, 1];

  for (let i = 2; i <= n; i++) {
    memo[i] = memo[i - 1] + memo[i - 2];
  }

  return memo[n];
}

console.log(fib(10, []), fibo(10)); // 55 55
