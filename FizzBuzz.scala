@main
def fizzBuzz() = {
  for(i <- 1 to 100) {
    var s = ""
    if(i % 3 == 0)  s += "Fizz"
    if(i % 5 == 0)  s += "Buzz"
    if(s == "")     s += i
    println(s)
  }
}
