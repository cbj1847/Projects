#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

#define MAX_COLUMN 100
#define MAX_DATA_LENGTH 100
#define MAX_DATA_NUM 100

typedef struct {
	char column[MAX_COLUMN];
	char data[MAX_DATA_NUM][MAX_DATA_LENGTH];

}Player;

typedef struct {
	char column[MAX_COLUMN];
	char data[MAX_DATA_NUM][MAX_DATA_LENGTH];

}Club;

typedef struct {
	char column[MAX_COLUMN];
	char data[MAX_DATA_NUM][MAX_DATA_LENGTH];

}League;

void set_table(Player* table_Player, Club* table_Club, League* table_League);
void get_all_element(Player* table_Player, Club* table_Club, League* table_League);
void print_all_table(Player* table_Player, Club* table_Club, League* table_League);
void find_element_by_key(Player* table_Player, Club* table_Club, League* table_League);




int main(void) {

	Player table_Player = { {0},{0} };
	Club table_Club = { {0},{0} };
	League table_League = { {0},{0} };

	Player* Table_p = &table_Player;
	Club* Table_c = &table_Club;
	League* Table_l = &table_League;

	set_table(Table_p, Table_c, Table_l);
	get_all_element(Table_p, Table_c, Table_l);
	print_all_table(Table_p, Table_c, Table_l);
	find_element_by_key(Table_p, Table_c, Table_l);
	


	return 0;
}

void set_table(Player* table_Player, Club* table_Club, League* table_League) {
	int fp_in_num = 0;
	FILE* fp1 = NULL, * fp2 = NULL, * fp3 = NULL;

	strcpy(table_Player->column, "key,p_name,club_key\n");
	strcpy(table_Club->column, "key,c_name,League_key\n");
	strcpy(table_League->column, "key,club_key1,club_key2,score\n");

	strcpy(table_Player->data[0], "1,손흥민,1\n");
	strcpy(table_Player->data[1], "2,박지성,2\n");
	strcpy(table_Player->data[2], "3,박주영,2\n");

	strcpy(table_Club->data[0], "1,토트넘,1\n");
	strcpy(table_Club->data[1], "2,맨유,1\n");
	strcpy(table_Club->data[2], "3,아스날,2\n");
	strcpy(table_Club->data[3], "4,맨시티,2\n");

	strcpy(table_League->data[0], "1,1,2,1:2\n");
	strcpy(table_League->data[1], "2,3,4,2:3\n");


	fp1 = fopen("Player.txt", "w");
	fp2 = fopen("Club.txt", "w");
	fp3 = fopen("League.txt", "w");

	fputs(table_Player->column, fp1);
	fputs(table_Club->column, fp2);
	fputs(table_League->column, fp3);


	for (fp_in_num = 0; fp_in_num < 3; fp_in_num++)
		fputs(table_Player->data[fp_in_num], fp1);


	for (fp_in_num = 0; fp_in_num < 4; fp_in_num++)
		fputs(table_Club->data[fp_in_num], fp2);


	for (fp_in_num = 0; fp_in_num < 2; fp_in_num++)
		fputs(table_League->data[fp_in_num], fp3);


	fclose(fp1);
	fclose(fp2);
	fclose(fp3);
}

void get_all_element(Player* table_Player, Club* table_Club, League* table_League) 
{
	int fp_in_num = 0;
	FILE* fp1 = NULL, * fp2 = NULL, * fp3 = NULL;
	char str[100];
	
	fp1 = fopen("Player.txt", "r");
	fp2 = fopen("Club.txt", "r");
	fp3 = fopen("League.txt", "r");

	fgets(str, 100, fp1);
	fgets(str, 100, fp2);
	fgets(str, 100, fp3);

	for (fp_in_num = 0; fp_in_num < 3; fp_in_num++)
		fgets(table_Player->data[fp_in_num],100, fp1);


	for (fp_in_num = 0; fp_in_num < 4; fp_in_num++)
		fgets(table_Club->data[fp_in_num],100, fp2);


	for (fp_in_num = 0; fp_in_num < 2; fp_in_num++)
		fgets(table_League->data[fp_in_num],100, fp3);

	fclose(fp1);
	fclose(fp2);
	fclose(fp3);
}



void print_all_table(Player* table_Player, Club* table_Club, League* table_League) {
	int p, c, l;
	printf("------Player_table-----\n");
	for (p = 0; table_Player != 0; p++)
	{
		if (p == 0)
			printf("%s", table_Player->column);
		else {
			if (table_Player->data[p - 1][0] == 0)
				break;
			printf("%s", table_Player->data[p - 1]);
		}
	}

	printf("------Club_table-----\n");
	for (c = 0; table_Club != 0; c++)
	{
		if (c == 0)
			printf("%s", table_Club->column);
		else {
			if (table_Club->data[c - 1][0] == 0)
				break;
			printf("%s", table_Club->data[c - 1]);
		}
	}

	printf("------League_table-----\n");
	for (l = 0; table_League != 0; l++)
	{
		if (l == 0)
			printf("%s", table_League->column);
		else {
			if (table_League->data[l - 1][0] == 0)
				break;
			printf("%s", table_League->data[l - 1]);
		}
	}
}


void find_element_by_key(Player* table_Player, Club* table_Club, League* table_League)
{
	int p, c, l;
	char str1[100] = { 0 };
	int num = 0;
	printf("어떤테이블을 사용하시겠습니까? (table_Player, table_Club, table_League) : ");
	gets(str1);
	printf("-----테이블 구성내용-----\n");
	
	{
	if (strcmp(str1, "table_Player")== 0)
	{
		for (p = 0; table_Player != 0; p++)
		{
			if (p == 0)
				printf("%s", table_Player->column);
			else {
				if (table_Player->data[p - 1][0] == 0)
					break;
				printf("%s", table_Player->data[p - 1]);
			}
		}

	}

	else if (strcmp(str1, "table_Club")==0 )
	{
		for (c = 0; table_Club != 0; c++)
		{
			if (c == 0)
				printf("%s", table_Club->column);
			else {
				if (table_Club->data[c - 1][0] == 0)
					break;
				printf("%s", table_Club->data[c - 1]);
			}
		}
	}

	else if (strcmp(str1, "table_League")==0)
	{
		for (l = 0; table_League != 0; l++)
		{
			if (l == 0)
				printf("%s", table_League->column);
			else {
				if (table_League->data[l - 1][0] == 0)
					break;
				printf("%s", table_League->data[l - 1]);
			}
		}
	}
	else
	{
		return 0;
	}
	}

	printf("\n연관된 자료를 찾을 key를 입력하십시오(0 = 종료) : ");
	scanf_s("%d", &num);
	{
		if (num == 0)
		{
			return 0;
		}

		else if (strcmp(str1, "table_Player") == 0 && num == 1)
		{
			printf("테이블 정보 : %s", table_Player->column);
			printf("선택된 데이터 : %s", table_Player->data[0]);
			printf("키 값으로 찾은 클럽정보 : %s", table_Club->data[0]);
		}

		else if (strcmp(str1, "table_Player") == 0 && num == 2)
		{
			printf("테이블 정보 : %s", table_Player->column);
			printf("선택된 데이터 : %s", table_Player->data[1]);
			printf("키 값으로 찾은 클럽정보 : %s", table_Club->data[1]);
		}

		else if (strcmp(str1, "table_Player") == 0 && num == 3)
		{
			printf("테이블 정보 : %s", table_Player->column);
			printf("선택된 데이터 : %s", table_Player->data[2]);
			printf("키 값으로 찾은 클럽정보 : %s", table_Club->data[1]);
		}

		else if (strcmp(str1, "table_Club") == 0 && num == 1)
		{
			printf("테이블 정보 : %s", table_Club->column);
			printf("선택된 데이터 : %s", table_Club->data[0]);
			printf("키 값으로 찾은 경기정보 : %s", table_League->data[0]);
		}

		else if (strcmp(str1, "table_Club") == 0 && num == 2)
		{
			printf("테이블 정보 : %s", table_Club->column);
			printf("선택된 데이터 : %s", table_Club->data[1]);
			printf("키 값으로 찾은 경기정보 : %s", table_League->data[0]);
		}

		else if (strcmp(str1, "table_Club") == 0 && num == 3)
		{
			printf("테이블 정보 : %s", table_Club->column);
			printf("선택된 데이터 : %s", table_Club->data[2]);
			printf("키 값으로 찾은 경기정보 : %s", table_League->data[1]);
		}
		
		else if (strcmp(str1, "table_Club") == 0 && num == 4)
		{
			printf("테이블 정보 : %s", table_Club->column);
			printf("선택된 데이터 : %s", table_Club->data[3]);
			printf("키 값으로 찾은 경기정보 : %s", table_League->data[1]);
		}

		else if (strcmp(str1, "table_League") == 0 && num == 1)
		{
			printf("\n테이블 정보 : %s\n", table_League->column);
			printf("선택된 데이터 : %s\n", table_League->data[0]);
			printf("키 값으로 찾은 클럽정보 : %s", table_Club->data[0]);
			printf("키 값으로 찾은 클럽정보 : %s", table_Club->data[1]);
		}
		
		else if (strcmp(str1, "table_League") == 0 && num == 2)
		{
			printf("\n테이블 정보 : %s\n", table_League->column);
			printf("선택된 데이터 : %s\n", table_League->data[1]);
			printf("키 값으로 찾은 클럽정보 : %s", table_Club->data[2]);
			printf("키 값으로 찾은 클럽정보 : %s", table_Club->data[3]);
		}

		else
		{
			return 0;
		}
	}
}


