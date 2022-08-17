let yourDate = new Date();
yourDate.toISOString().split("T")[0];
const offset = yourDate.getTimezoneOffset();
yourDate = new Date(yourDate.getTime() - offset * 60 * 1000);
console.log(yourDate.toISOString().split("T")[0]);
