for (let i = 1; i <= 100; i++) {
  let s = "";
  if (!(i % 3)) s += "Fizz";
  if (!(i % 5)) s += "Buzz";
  console.log(s || i);
}
