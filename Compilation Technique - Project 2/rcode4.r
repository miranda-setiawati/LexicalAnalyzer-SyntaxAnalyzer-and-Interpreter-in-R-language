#R version 3.4.4
cat("List of Odd Number 1-100: \n");
num <- 1;
while (num <= 100) {
    sisa <- (num % 2);
    if (sisa != 0) {
        oddnum <- num;
        cat(oddnum, " ");
    };
    num <- num + 1;
}