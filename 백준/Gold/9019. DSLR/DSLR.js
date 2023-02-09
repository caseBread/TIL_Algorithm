const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let ipcount = 0;
let t;

rl.on("line", function (line) {
  if (ipcount === 0) {
    t = Number(line);
  } else {
    var [num, end] = line.split(" ").map(Number);
    console.log(solution(num, end));
  }
  if (ipcount == Number(t)) {
    rl.close();
  }
  ipcount += 1;
}).on("close", function () {
  process.exit();
});

function calD(num) {
  if (num * 2 >= 10000) {
    return num * 2 - 10000;
  } else {
    return num * 2;
  }
}

function calS(num) {
  if (num === 0) {
    return 9999;
  } else {
    return num - 1;
  }
}

function calL(num) {
  let str = String(num).padStart(4, "0");
  let convertStr = str.substring(1) + str.substring(0, 1);
  return Number(convertStr);
}

function calR(num) {
  let str = String(num).padStart(4, "0");
  let convertStr = str.substring(3) + str.substring(0, 3);
  return Number(convertStr);
}

function bfs(num, end) {
  const visited = new Array(10000).fill(false);
  const queue = [];
  queue.push([num, ""]);
  visited[num] = true;
  while (queue.length !== 0) {
    const [nowNum, nowPattern] = queue.shift();

    const convertNums = [
      [calD(nowNum), "D"],
      [calS(nowNum), "S"],
      [calL(nowNum), "L"],
      [calR(nowNum), "R"],
    ];
    let ok = false;
    let result;
    convertNums.forEach((x, idx) => {
      const [convertNum, pattern] = x;
      if (!visited[convertNum]) {
        if (convertNum === end) {
          ok = true;
          result = nowPattern + pattern;
          return;
        }
        visited[convertNum] = true;
        queue.push([convertNum, nowPattern + pattern]);
      }
    });
    if (ok) {
      return result;
    }
  }
}

function solution(num, end) {
  return bfs(num, end);
}
