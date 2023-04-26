impl Solution {
    pub fn add_digits(num: i32) -> i32 {
        let mut num = num;
        while num > 9 {
            let mut new_num = 0;
            while num > 0 {
                new_num += num % 10;
                num /= 10;
            }
            num = new_num;
        }
        
        num
    }
}