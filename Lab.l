%{
#include <stdio.h>
%}

%%
[0-9]+    { printf("Integer: %s\n", yytext); }
[ \t\n]+  { /* skip whitespace */ }
.         { printf("Invalid character: %s\n", yytext); }
%%

int main() {
    printf("Enter input (press Ctrl+D or Ctrl+Z to end):\n");
    yylex();   // call lexical analyzer to process input
    return 0;
}

int yywrap() {
    return 1;   // end of input
}
