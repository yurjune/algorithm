const isPrime = (num) => {
  if (num <= 1) return false;
  if (num % 2 === 0) return num === 2;

  for (let i = 3; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }

  return true;
};

console.log(isPrime(17)); // true
