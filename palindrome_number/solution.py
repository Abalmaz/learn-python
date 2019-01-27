bool isPalindrome(int x) {
    bool polindrome = true;
    if (x < 0)
    {
        polindrome = false;
    }
    int num = x;
    int reverse = 0;
    while (num > 0)
    {
        reverse = reverse*10 + num%10;
        num /= 10;
    }
    if (reverse != x)
    {
        polindrome = false;
    }
    return polindrome;
}
