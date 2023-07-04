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
		direction = rand() % 4 + 1; // ������ [2,2] ���������κ��� 1�� 2�� 3�� 4�� ���� �̵�

		switch (direction) // �����ϰ� �Է¹��� direction�� case 1~4�� ���� �ش��������� �̵� ��
			               //  �ش� �迭�� ��簪�� point�� �ջ� �� �迭�� 9���� ����
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
	if (num > 5) // ����Ƚ�� 5ȸ �̻��ΰ�� �й�
	{
		looseGame();
	}
	else if (Point_x == 0 && direction == 3) // x�� 0, 1���϶� direction3�� �������� �Ѿ�� �й�
	{
		looseGame();
	}
	else if (Point_x == 4 && direction == 4) // x�� 4, 5���϶� direction4�� �������� �Ѿ�� �й�
	{
		looseGame();
	}
	else if (Point_y == 0 && direction == 1) // y�� 0, 1���϶� direction1�� ������� �Ѿ�� �й�
	{
		looseGame();
	}
	else if (Point_y == 4 && direction == 2) // y�� 4, 5���϶� direction2�� �ϴ����� �Ѿ�� �й�
	{
		looseGame();
	}
}

void checkWin(int Point_x, int Point_y)
{
	if (point > 9) // loosegame�� �׻� ���� üũ�ϹǷ� if - else�� �������� ����Ƚ�� num�� �����������, ����Ʈ10���̻��Ͻ� �¸�
	{
		winGame();
	}
}

void winGame()
{
	system("cls");
	printf("------------------\n");
	printf("���ӿ��� �¸��ϼ̽��ϴ�.\n");
	printf("�� ���� : %d\n", point);
	printf("�� Ƚ�� : %d\n", num);
	printf("------------------\n");
	exit(0);
}

void looseGame()
{
	system("cls");
	printf("------------------\n");
	printf("���ӿ��� �й��ϼ̽��ϴ�.\n");
	printf("�� ���� : %d\n", point);
	printf("�� Ƚ�� : %d\n", num);
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
	printf("���� :  %d \n", direction);
	printf("���� :  %d \n", point);
	printf("Ƚ�� :  %d \n", num);
	printf("------------------\n");
	Sleep(2000);
}