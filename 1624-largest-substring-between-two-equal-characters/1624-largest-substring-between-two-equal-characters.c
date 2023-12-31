int maxLengthBetweenEqualCharacters(char* s) {
    int seen[26];
    for (int i = 0; i < 26; i++) {
        seen[i] = -1;
    }
    
    int ch;
    int ans = -1;
    for (int i = 0; i < strlen(s); i++) {
        ch = s[i] - 'a';
        if (seen[ch] == -1) {
            seen[ch] = i;
        } else if (ans < i - seen[ch] - 1) {
            ans = i - seen[ch] - 1;
        }
    }
    
    return ans;
}