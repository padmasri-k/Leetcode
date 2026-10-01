bool isValid(char* str) {
    int top=-1;
    char stack[11111];
    int i;
    for (i=0;str[i]!='\0';i++){
        if(str[i]=='{'|| str[i]=='['||str[i]=='('){
            top++;
            stack[top]=str[i];
        }
        else{
            if(top>=0 && (
            (str[i]=='}' && stack[top]=='{')||
            (str[i]==']' && stack[top]=='[')||
            (str[i]==')' && stack[top]=='(')
            )){
                top--;
            }
            else{
                return false;
            }
            }
        }
        return top==-1;

}