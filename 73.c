#include <stdio.h>
int main(void)
{
	int a,b,c;
	scanf("%d %d %d",&a,&b,&c);
	if((a>b)&&(a<c))
	{
		printf("yes");
	}
	else
	printf("no");
	return 0;
}
