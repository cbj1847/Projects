#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <Windows.h>


#define Width  5
#define Depth  5


void mapCreate(int map[][Depth]);
void playGame(int Point_x, int Point_y, int map[][Depth]);
void mapPrint(int map[][Depth]);
void checkLoose(int Point_x, int Point_y);
void checkWin(int Point_x, int Point_y);
void looseGame();
void winGame();


int num = 0;
int point = 0;
int direction;

int main()
{
	int humanPoint_x = 2;
	int humanPoint_y = 2;

	int map[Width][Depth] = { 0, };

	mapCreate(map);
	mapPrint(map);
	playGame(humanPoint_x, humanPoint_y, map);

	return 0;
}

void mapCreate(int map[][Depth])
{
	srand(time(NULL));
	for (int i = 0; i < 5; i++)
	{
		for (int j = 0; j < 5; j++)
		{

			if (rand() % 3)
				map[i][j] = rand() % 9;
		}
	}
	map[2][2] = 9;
}

void playGame(int Point_x, int Point_y, int map[][Depth])
{
	srand(time(NULL));
	num = 0;
		

	while (num <10)
	{
		checkLoose(Point_y, Point_x);
		checkWin(Point_y, Point_x);
		direction = rand() % 4 + 1; // 방향을 [2,2] 시작점으로부터 1상 2하 3좌 4우 랜덤 이동

		switch (direction) // 랜덤하게 입력받은 direction을 case 1~4에 따라 해당지점으로 이동 및
			               //  해당 배열의 배당값을 point에 합산 후 배열에 9값을 저장
		{
		case 1:
		{
			Point_y -= 1;
			num++;
			
			if (map[Point_y][Point_x] != 9)
			{
				point += map[Point_y][Point_x];
				map[Point_y][Point_x] = 9;
				mapPrint(map);
				break;
			}
			else
			{
				mapPrint(map);
				break;
			}
		}

		case 2:
		{
			Point_y += 1;
			num++;
			
			if (map[Point_y][Point_x] != 9)
			{
				point += map[Point_y][Point_x];
				map[Point_y][Point_x] = 9;
				mapPrint(map);
				break;
			}
			else
			{
				mapPrint(map);
				break;
			}
			
		}

		case 3:
		{
			Point_x -= 1;
			num++;
			
			if (map[Point_y][Point_x] != 9)
			{
				point += map[Point_y][Point_x];
				map[Point_y][Point_x] = 9;
				mapPrint(map);
				break;
			}
			else
			{
				mapPrint(map);
				break;
			}
			
		}

		case 4:
		{
			Point_x += 1;
			num++;
			
			if (map[Point_y][Point_x] != 9)
			{
				point += map[Point_y][Point_x];
				map[Point_y][Point_x] = 9;
				mapPrint(map);
				break;
			}
			else
			{
				mapPrint(map);
				break;
			}
			
		}
		}
	}
}


void checkLoose(int Point_x, int Point_y)
{
	if (num > 5) // 시행횟수 5회 이상인경우 패배
	{
		looseGame();
	}
	else if (Point_x == 0 && direction == 3) // x가 0, 1열일때 direction3인 좌측으로 넘어가면 패배
	{
		looseGame();
	}
	else if (Point_x == 4 && direction == 4) // x가 4, 5열일때 direction4인 우측으로 넘어가면 패배
	{
		looseGame();
	}
	else if (Point_y == 0 && direction == 1) // y가 0, 1행일때 direction1인 상단으로 넘어가면 패배
	{
		looseGame();
	}
	else if (Point_y == 4 && direction == 2) // y가 4, 5행일때 direction2인 하단으로 넘어가면 패배
	{
		looseGame();
	}
}

void checkWin(int Point_x, int Point_y)
{
	if (point > 9) // loosegame을 항상 먼저 체크하므로 if - else의 개념으로 시행횟수 num은 고려하지않음, 포인트10점이상일시 승리
	{
		winGame();
	}
}

void winGame()
{
	system("cls");
	printf("------------------\n");
	printf("게임에서 승리하셨습니다.\n");
	printf("총 점수 : %d\n", point);
	printf("총 횟수 : %d\n", num);
	printf("------------------\n");
	exit(0);
}

void looseGame()
{
	system("cls");
	printf("------------------\n");
	printf("게임에서 패배하셨습니다.\n");
	printf("총 점수 : %d\n", point);
	printf("총 횟수 : %d\n", num);
	printf("------------------\n");
	exit(0);
}

void mapPrint(int map[][Depth])
{
	system("cls");
	printf("------------------\n");
	for (int i = 0; i < 5; i++)
	{
		for (int j = 0; j < 5; j++)
		{
			if (map[i][j] == 9)
				printf("X ");
			else
				printf("%d ", map[i][j]);
		}
		printf("\n");

	}
	printf("------------------\n");
	printf("방향 :  %d \n", direction);
	printf("점수 :  %d \n", point);
	printf("횟수 :  %d \n", num);
	printf("------------------\n");
	Sleep(2000);
}