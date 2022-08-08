fn count_bits(n: i32) -> i32 {
    let mut count = 0;
    let mut n = n;
    while (n > 0) {
        count += n & 1;
        n >>= 1;
    }
    count
}

impl Solution {
    pub fn count_bits(n: i32) -> Vec<i32> {
        (0..=n).map(count_bits).collect()
    }
}