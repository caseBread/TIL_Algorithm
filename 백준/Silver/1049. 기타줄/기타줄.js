const { exit } = require("process");
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let ipcount = 0;
let input = [];
let n;
let m;

rl.on("line", function (line) {
  if (ipcount === 0) {
    [n, m] = line.split(" ").map(Number);
  } else {
    input.push(line.split(" ").map(Number));
  }
  if (ipcount == Number(m)) {
    console.log(solution());
    rl.close();
  }
  ipcount += 1;
}).on("close", function () {
  process.exit();
});

function solution() {
  let minn6 = 1000000000;
  let minn0_5 = 1000000000;
  for (let i = 0; i < m; i++) {
    minn6 = input[i][0] < minn6 ? input[i][0] : minn6;
    minn6 = input[i][1] * 6 < minn6 ? input[i][1] * 6 : minn6;
    minn0_5 = input[i][0] < minn0_5 ? input[i][0] : minn0_5;
    minn0_5 = input[i][1] * (n % 6) < minn0_5 ? input[i][1] * (n % 6) : minn0_5;
  }
  return minn6 * parseInt(n / 6) + minn0_5;
}
