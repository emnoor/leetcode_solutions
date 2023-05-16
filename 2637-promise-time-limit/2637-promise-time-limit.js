async function sleep(millis) {
    return new Promise((resolve, reject) => {
        setTimeout(() => resolve({success: false, value: "Time Limit Exceeded"}), millis);
    });
}

async function wrapper(fn, args) {
    try {
        const r = await fn(...args);
        return {success: true, value: r};
    } catch (err) {
        return {success: false, value: err};
    }
}

/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
	return async function(...args) {
        const r = await Promise.any([wrapper(fn, args), sleep(t)]);
        if (r.success === false)
            throw r.value;
        else
            return r.value;
    }
};


/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */