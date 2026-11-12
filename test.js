const _ = require("lodash");
const assert = require("assert");

assert.deepStrictEqual(_.chunk([1, 2, 3, 4], 2), [[1, 2], [3, 4]]);
console.log("lodash", _.VERSION, "test passed");