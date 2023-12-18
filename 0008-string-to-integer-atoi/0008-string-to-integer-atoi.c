int myAtoi(char* s) {
    int min = -2147483648;
    int max = 2147483647;
    int len = strlen(s);
    long long n = 0;
    int i = 0;
    int sign = 1;
    
    // whitespace
    for (; i < len; i++) {
        if (s[i] != ' ') {
            break;
        }
    }
    
    // sign
    if (i < len) {
        if (s[i] == '+') {
            i += 1;
        } else if (s[i] == '-') {
            i += 1;
            sign = -1;
        }
    }
    
    // digits
    for (; i < len; i++) {
        if (s[i] >= '0' && s[i] <= '9') {
            n = n * 10 + sign * (s[i] - '0');
            if (n > max) {
                n = max;
                break;
            }
            if (n < min) {
                n = min;
                break;
            }
        } else {
            break;
        }
    }
    
    return n;
}