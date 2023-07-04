#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Windows.h>

#define MAX_NAME_LENGTH 20	//process�� �̸��� ũ��
#define PROCESS_NUM 5	//

//process_struct ����
typedef struct processStruct {

	char* name;			//process�� �̸�
	int priority;		//process�� �켱����
	int leftoverTime;	//process�� �ܿ��ð�
	int performTime;	//process�� ����ð�
	int arrivalTime;	//process�� �����ð�

}processStruct;

processStruct* createProcess(char* name, int priority, int performTime, int arrivalTime);	//���ο� process�� �����ϴ� �Լ�
void sort(processStruct* process[]);	// �����ð� ������ �������ִ� �Լ�
void display(processStruct* process[], int num, int time, int work);	//���� ���¸� ����ϴ� �Լ�

void FCFS(processStruct* process[]);
void SJF(processStruct* process[]);
void PRIORITY(processStruct* process[]);
void SRT(processStruct* process[]);
void RR(processStruct* process[]);

int main(void)
{
	processStruct* process_[PROCESS_NUM];
	char name_temp[MAX_NAME_LENGTH];
	int priority_temp;
	int leftovertime_temp;
	int performtime_temp;
	int arrivaltime_temp;
	int time = 0;
	int input;

	// �ټ����� process ����
	for (int i = 0; i < 5; i++)
	{
		printf("PROCESS�� �����ϼ���. ");
		scanf("%s %d %d %d", name_temp, &priority_temp, &performtime_temp, &arrivaltime_temp);
		process_[i] = createProcess(name_temp, priority_temp, performtime_temp, arrivaltime_temp);
	}

	//�����ٸ� ��� ����
	printf("�����ٸ� ����� �����ϼ���.\n");
	printf("1. FCFS, 2. SJF, 3. PRIORITY, 4. SRT, 5. RR :");
	scanf("%d", &input);

	switch (input) {
	case 1:
		FCFS(process_);
		break;
	case 2:
		SJF(process_);
		break;
	case 3:
		PRIORITY(process_);
		break;
	case 4:
		SRT(process_);
		break;
	case 5:
		RR(process_);;
		break;
	}

	return 0;
}
// non-preemptive

void FCFS(processStruct* process[]) {
	processStruct* temp;
	int t = 0;
	int check;
	int work = 0;
	int currentProcess = 0;
	sort(process);	//�����ð� ������ �迭�� ����

	while (1)
	{
		system("cls");
		// process�� �����ð��� ����ð� ���� ū�� Ȯ��
		if (process[currentProcess]->arrivalTime > t)
		{
			// ���� �������� ���� �����̹Ƿ� �ش� ���� ���
			work = 0;
			display(process, currentProcess, t, work);
		}
		else
		{
			// process�� ������ ��� 
			work = 1;

			// ��� process�� �ܿ� �ð��� 0���� Ȯ��
			check = 0;
			for (int i = 0; i < 5; i++)
			{
				check += process[i]->leftoverTime;
			}
			// ��� process�� ����� ���
			if (check <= 0)
			{
				work = -1;
				display(process, currentProcess, t, work);
				break;
			}

			// ���� �������� process�� ����� ���
			if (process[currentProcess]->leftoverTime == 0)
			{
				//�������̴� process�� ������ process�� ����
				if (currentProcess == 4)
				{
					work = -1;
					display(process, currentProcess, t, work);
					break;
				}
				currentProcess += 1;
				continue;
			}

			// ���� ���� ��� �� ���� �������� process�� �ܿ��ð� 1 ����
			display(process, currentProcess, t, work);
			process[currentProcess]->leftoverTime -= 1;
		}

		// ���� �ð� 1 ����
		t++;
		Sleep(2000);
	}

	// ��� process�� ����Ǹ� malloc���� �Ҵ����� memory �Ҵ�����
	for (int i = 0; i < 5; i++)
	{
		free(process[i]);
	}

}


// ����ð� ���� �ִ� 100
void SJF(processStruct* process[]) {

	processStruct* temp;
	int t = 0;
	int work = 0;
	int currentProcess = 0;
	int min = 100;
	int check1;
	int check2 = 0;
	sort(process);	//�����ð� ������ �迭�� ����


	while (1)
	{
		system("cls");
		// process�� �����ð��� ����ð� ���� ū�� Ȯ��
		if (process[currentProcess]->arrivalTime > t)
		{
			// ���� �������� ���� �����̹Ƿ� �ش� ���� ���
			work = 0;
			display(process, currentProcess, t, work);
		}
		else
		{
			// process�� ������ ��� 
			work = 1;

			if (process[currentProcess]->leftoverTime == 0)
			{
				// ���� �������̴� process�� ������ �Ϸ�Ǿ��� ���

				// ����ð��� ���� ���� process ã��
				for (int i = 0; i < 5; i++)
				{
					// ���� �������� �ʾҰų� ������ �Ϸ�� process�� ����
					if (process[i]->leftoverTime == 0 || process[i]->arrivalTime > t)
					{
						continue;
					}
					// ������ process �� 
					else if (process[i]->performTime < min)
					{
						// min���� ���� ���� ���� �ð��� ���� process�� ���� process�� ����
						min = process[i]->performTime;
						currentProcess = i;
					}
				}
				min = 100;

				// �� ������ Ŀ�������� ���� process�� �ܿ� �ð��� 0�� ���, ���� ���� proecess�� �������� �ʾҰų� ��� process�� ����� ���
				if (process[currentProcess]->leftoverTime == 0)
				{
					// ��� process�� �ܿ��ð��� Ȯ���Ͽ� ��� process�� ����Ǿ����� Ȯ��
					check1 = 0;
					for (int i = 0; i < 5; i++)
					{
						check1 += process[i]->leftoverTime;
					}
					if (check1 == 0)
					{
						// ��� process�� ����Ǿ��ٸ� ���α׷� ����
						work = -1;
						display(process, currentProcess, t, work);
						break;
					}
					// ��� process�� �ܿ��ð��� 0�̰ų� ���� ������ process�� ���� ���
					for (int i = 0; i < 5; i++)
					{
						if (process[i]->leftoverTime == 0 || process[i]->arrivalTime > t)
						{
							check2 += 1;
							continue;
						}
					}
					if (check2 == 5)
					{
						// ���� process�� ���ٴ� ���¸� ����ϰ� ���� �ð��� 1����
						system("cls");
						work = 0;
						check2 = 0;
						display(process, currentProcess, t, work);
						t++;
						Sleep(2000);
						continue;
					}
				}
			}
			// ���� �ܿ��ð��� 0�� �ƴϰ� process�� �������� ��� ���� ���� ����ϰ� �ܿ��ð� 1 ����
			display(process, currentProcess, t, work);
			process[currentProcess]->leftoverTime -= 1;
		}
		// ���� �ð� 1����
		t++;
		Sleep(2000);
	}

	// ��� process�� ����Ǹ� malloc���� �Ҵ����� �޸𸮸� ����
	for (int i = 0; i < 5; i++)
	{
		free(process[i]);
	}

}


//����
void PRIORITY(processStruct* process[])
{
	processStruct* temp;
	int max = 100;
	int max1 = 0;
	int t = 0;
	int check1;
	int check2 = 0;
	int work = 0;
	int currentProcess = 0;
	sort(process);	//�����ð� ������ �迭�� ����

	while (1)
	{
		system("cls");
		// process�� �����ð��� ����ð� ���� ū�� Ȯ��
		if (process[currentProcess]->arrivalTime > t)
		{
			// ���� �������� ���� �����̹Ƿ� �ش� ���� ���
			work = 0;
			display(process, currentProcess, t, work);
		}
		else
		{
			// process�� ������ ��� 
			work = 1;

			// �켱������ ���� ���� process ã��
			for (int j = 0; j < 5; j++)
			{
				// ���� �������� �ʾҰų� ������ �Ϸ�� process�� ����
				if (process[j]->leftoverTime == 0 || process[j]->arrivalTime > t)
				{
					continue;
				}
				// ������ process �� 
				else if (process[j]->priority <= max)
				{
					// �켱������ ������ �������� process�� ���� process�� ����
					if (process[j]->priority == max)
					{
						currentProcess = max1;
					}
					// max���� ��������(�켱����������) �켱������ ���� process�� ���� process�� ����
					else
					{
						max = process[j]->priority;
						max1 = j;
						currentProcess = j;
					}
				}
				
			}
				max = 100;
			

				// ���� process�� �ܿ� �ð��� 0�� ��쿡 ���� ���� proecess�� �������� �ʾҰų���� process�� ����� ���
				if (process[currentProcess]->leftoverTime == 0)
				{
					// ��� process�� �ܿ��ð��� Ȯ���Ͽ� ��� process�� ����Ǿ����� Ȯ��
					check1 = 0;
					for (int i = 0; i < 5; i++)
					{
						check1 += process[i]->leftoverTime;
					}
					if (check1 == 0)
					{
						// ��� process�� ����Ǿ��ٸ� ���α׷� ����
						work = -1;
						display(process, currentProcess, t, work);
						break;
					}
					// ��� process�� �ܿ��ð��� 0�̰ų� ���� ������ process�� ���� ���
					for (int i = 0; i < 5; i++)
					{
						if (process[i]->leftoverTime == 0 || process[i]->arrivalTime > t)
						{
							check2 += 1;
							continue;
						}
					}
					if (check2 == 5)
					{
						// ���� process�� ���ٴ� ���¸� ����ϰ� ���� �ð��� 1����
						system("cls");
						work = 0;
						check2 = 0;
						display(process, currentProcess, t, work);
						t++;
						Sleep(2000);
						continue;
					}
				}

				// ���� ���� ��� �� ���� �������� process�� �ܿ��ð� 1 ����
				display(process, currentProcess, t, work);
				process[currentProcess]->leftoverTime -= 1;
		}

			// ���� �ð� 1 ����
			t++;
			Sleep(2000);
	}

		// ��� process�� ����Ǹ� malloc���� �Ҵ����� memory �Ҵ�����
		for (int i = 0; i < 5; i++)
		{
			free(process[i]);
		}

}

void SRT(processStruct* process[]) 
{

	processStruct* temp;
	int t = 0;
	int work = 0;
	int currentProcess = 0;
	int lot = 100;
	int lot1 = 0;
	int check1;
	int check2 = 0;
	sort(process);	//�����ð� ������ �迭�� ����

	while (1)
	{
		system("cls");
		// process�� �����ð��� ����ð� ���� ū�� Ȯ��
		if (process[currentProcess]->arrivalTime > t)
		{
			// ���� �������� ���� �����̹Ƿ� �ش� ���� ���
			work = 0;
			display(process, currentProcess, t, work);
		}
		else
		{
				// process�� ������ ��� 
				work = 1;
				// ����ð��� ���� ���� process ã��
				for (int k = 0; k < 5; k++)
				{
					// ���� �������� �ʾҰų� ������ �Ϸ�� process�� ����
					if (process[k]->leftoverTime == 0 || process[k]->arrivalTime > t)
					{
						continue;
					}
					// ������ process �� 
					else if (process[k]->leftoverTime <= lot)
					{
						//lot�� �ܿ��ð��� ���� process�� ������ �켱���� ���� �ͺ��� ����
						if (process[k]->leftoverTime == lot)
						{
							currentProcess = lot1;
						}
						// lot���� ���� ���� �ܿ� �ð��� ���� process�� ���� process�� ����
						else
						{
							lot = process[k]->leftoverTime;
							lot1 = k;
							currentProcess = k;
						}
					}
				}
				lot = 100;

				// �� ������ ���������� ���� process�� �ܿ� �ð��� 0�� ���, ���� ���� proecess�� �������� �ʾҰų� ��� process�� ����� ���
				if (process[currentProcess]->leftoverTime == 0)
				{
					// ��� process�� �ܿ��ð��� Ȯ���Ͽ� ��� process�� ����Ǿ����� Ȯ��
					check1 = 0;
					for (int i = 0; i < 5; i++)
					{
						check1 += process[i]->leftoverTime;
					}
					if (check1 == 0)
					{
						// ��� process�� ����Ǿ��ٸ� ���α׷� ����
						work = -1;
						display(process, currentProcess, t, work);
						break;
					}
					// ��� process�� �ܿ��ð��� 0�̰ų� ���� ������ process�� ���� ���
					for (int i = 0; i < 5; i++)
					{
						if (process[i]->leftoverTime == 0 || process[i]->arrivalTime > t)
						{
							check2 += 1;
							continue;
						}
					}
					if (check2 == 5)
					{
						// ���� process�� ���ٴ� ���¸� ����ϰ� ���� �ð��� 1����
						system("cls");
						work = 0;
						check2 = 0;
						display(process, currentProcess, t, work);
						t++;
						Sleep(2000);
						continue;
					}
				}
		
			// ���� �ܿ��ð��� 0�� �ƴϰ� process�� �������� ��� ���� ���� ����ϰ� �ܿ��ð� 1 ����
			display(process, currentProcess, t, work);
			process[currentProcess]->leftoverTime -= 1;
		}
		// ���� �ð� 1����
		t++;
		Sleep(2000);
	}

		// ��� process�� ����Ǹ� malloc���� �Ҵ����� �޸𸮸� ����
		for (int i = 0; i < 5; i++)
		{
		free(process[i]);
		}

}

void RR(processStruct* process[]) 
{
	
	processStruct* temp;
	int projectnum = 0;
	int h;
	int t = 0;
	int check;
	int work = 0;
	int currentProcess = 0;
	sort(process);

	while (1)
	{
		system("cls");
		// process�� �����ð��� ����ð� ���� ū�� Ȯ��
		if (process[currentProcess]->arrivalTime > t)
		{
			// ���� �������� ���� �����̹Ƿ� �ش� ���� ���
			work = 0;
			display(process, currentProcess, t, work);
		}
		else
		{
			// process�� ������ ��� 
			work = 1;
			
		
			// ��� process�� �ܿ� �ð��� 0���� Ȯ��
			check = 0;
			for (int i = 0; i < 5; i++)
			{
				check += process[i]->leftoverTime;
			}
			// ��� process�� ����� ���
			if (check <= 0)
			{
				work = -1;
				display(process, currentProcess, t, work);
				break;
			}
			
			// ���� ���� ��� �� ���� �������� process�� �ܿ��ð� 1 ����, 2�ʸ��� ���� process�� �Ѿ
			if (process[currentProcess]->leftoverTime > 0)
			{
				if (t % 2 == 0)
				{
					if (currentProcess == 4)
					{
						display(process, currentProcess, t, work);
						process[currentProcess]->leftoverTime -= 1;
						currentProcess = 0;
					}
					else
					{
						currentProcess += 1;
						display(process, currentProcess, t, work);
						process[currentProcess]->leftoverTime -= 1;
					}
				}
				else
				{
					display(process, currentProcess, t, work);
					process[currentProcess]->leftoverTime -= 1;
				}
			}
			// ���� �������� process�� ����Ǹ� ���� process�� �Ѿ�� ���� ���
			else if (process[currentProcess]->leftoverTime == 0)
			{
				currentProcess += 1;
				display(process, currentProcess, t, work);
			}
		}
		// ���� �ð� 1 ����
		t++;
		Sleep(2000);
	}

	// ��� process�� ����Ǹ� malloc���� �Ҵ����� memory �Ҵ�����
	for (int i = 0; i < 5; i++)
	{
		free(process[i]);
	}
	
}


// �迭�� process���� �����ð� ������ ����
void sort(processStruct* process[]) {

	processStruct* temp;

	int i, j;

	for (i = 4; i > 0; i--) {
		for (j = 0; j < i; j++) {
			if (process[j]->arrivalTime > process[j + 1]->arrivalTime) {
				temp = process[j + 1];
				process[j + 1] = process[j];
				process[j] = temp;
			}
		}
	}

	printf("%d %d %d", process[0]->arrivalTime, process[1]->arrivalTime, process[2]->arrivalTime);

}

// ���� ���¸� ������ִ� �Լ�
void display(processStruct* process[], int num, int time, int work) {
	switch (work) {

	case 0:
		printf("�ð�: %d\b\n", time);
		printf("==================================================================================================================\n");
		printf("���� �������� process�� �����ϴ�.\b\n");
		printf("==================================================================================================================\n\n");
		for (int i = 0; i < 5; i++)
		{
			printf("Process : %s, Priority : %d, PerformTime : %d, ArrivalTime : %d, RemainingTime : %d \n", process[i]->name, process[i]->priority, process[i]->performTime, process[i]->arrivalTime, process[i]->leftoverTime);
		}
		break;


	case 1:
		printf("�ð�: %d\b\n", time);
		printf("==================================================================================================================\n");
		printf("���� �������� process�� �̸���: %s\b\n", process[num]->name);
		printf("==================================================================================================================\n\n");
		for (int i = 0; i < 5; i++)
		{
			printf("Process : %s, Priority : %d, PerformTime : %d, ArrivalTime : %d, RemainingTime : %d \n", process[i]->name, process[i]->priority, process[i]->performTime, process[i]->arrivalTime, process[i]->leftoverTime);
		}
		break;
	case -1:
		printf("�ð�: %d\b\n", time);
		printf("==================================================================================================================\n");
		printf("��� process�� ����Ǿ����ϴ�. \b\n");
		printf("==================================================================================================================\n\n");
		break;
	}


}


// process�� �������ִ� �Լ�
processStruct* createProcess(char* name, int priority, int performTime, int arrivalTime) {
	char* tempProcessName = (char*)malloc(sizeof(char) * MAX_NAME_LENGTH);
	processStruct* tempProcessStruct = (processStruct*)malloc(sizeof(processStruct));

	if (tempProcessName == NULL || tempProcessStruct == NULL)
	{
		perror("�޸� �Ҵ� ����");
		exit(1);
	}
	else
	{
		strcpy(tempProcessName, name);
		tempProcessStruct->name = tempProcessName;
		tempProcessStruct->priority = priority;
		tempProcessStruct->performTime = performTime;
		tempProcessStruct->arrivalTime = arrivalTime;
		tempProcessStruct->leftoverTime = performTime;

		return tempProcessStruct;
	}

}