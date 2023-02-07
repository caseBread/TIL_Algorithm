const { exit } = require("process");
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", function (line) {
  console.log(solution(line));

  rl.close();
}).on("close", function () {
  process.exit();
});

function solution(input) {
  let dp;
  (dp = []).length = input.length + 1;
  dp.fill(0);

  dp[0] = 1;

  if (Number(input.substr(0, 1)) === 0) {
    console.log(0);
    exit();
  }
  dp[1] = 1;

  for (let i = 2; i <= input.length; i++) {
    //   console.log(Number(input.substr(i - 2, 2)));
    if (
      Number(input.substr(i - 1, 1)) === 0 &&
      Number(input.substr(i - 2, 2)) !== 10 &&
      Number(input.substr(i - 2, 2)) !== 20
    ) {
      console.log(0);
      exit();
    }
    if (
      11 <= Number(input.substr(i - 2, 2)) &&
      Number(input.substr(i - 2, 2)) <= 26 &&
      Number(input.substr(i - 2, 2)) !== 20
    ) {
      dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000;
    } else if (
      Number(input.substr(i - 2, 2)) === 20 ||
      Number(input.substr(i - 2, 2)) === 10
    ) {
      dp[i] = dp[i - 2];
    } else {
      dp[i] = dp[i - 1];
    }
  }

  return dp[input.length];
}
