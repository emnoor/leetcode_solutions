async function worker(functions) {
    while (1) {
        let fn = functions.pop();
        if (fn === undefined)
            break;
        await fn();
    }
};

/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Function}
 */
var promisePool = async function(functions, n) {
    functions.reverse();
    
    let workers = [];
    for (let i = 0; i < n; i++) {
        workers.push(worker(functions))
    }
    
    return Promise.all(workers);
};

/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */