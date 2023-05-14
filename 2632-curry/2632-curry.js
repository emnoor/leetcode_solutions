/**
 * @param {Function} fn
 * @return {Function}
 */
var curry = function(fn) {
    const arg = [];
    return function curried() {
        arg.push(...arguments);
        if (arg.length >= fn.length) {
            return fn(...arg);
        } else {
            return curried;
        }
    };
};

/**
 * function sum(a, b) { return a + b; }
 * const csum = curry(sum);
 * csum(1)(2) // 3
 */
