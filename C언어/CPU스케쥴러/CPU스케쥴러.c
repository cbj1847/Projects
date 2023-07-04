#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Windows.h>

#define MAX_NAME_LENGTH 20	//process의 이름의 크기
#define PROCESS_NUM 5	//

//process_struct 정의
typedef struct processStruct {

	char* name;			//process의 이름
	int priority;		//process의 우선순위
	int leftoverTime;	//process의 잔여시간
	int performTime;	//process의 수행시간
	int arrivalTime;	//process의 도착시간

}processStruct;

processStruct* createProcess(char* name, int priority, int performTime, int arrivalTime);	//새로운 process를 생성하는 함수
void sort(processStruct* process[]);	// 도착시간 순서로 정렬해주는 함수
void display(processStruct* process[], int num, int time, int work);	//현재 상태를 출력하는 함수

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

	// 다섯개의 process 생성
	for (int i = 0; i < 5; i++)
	{
		printf("PROCESS를 생성하세요. ");
		scanf("%s %d %d %d", name_temp, &priority_temp, &performtime_temp, &arrivaltime_temp);
		process_[i] = createProcess(name_temp, priority_temp, performtime_temp, arrivaltime_temp);
	}

	//스케줄링 방법 선택
	printf("스케줄링 방법을 선택하세요.\n");
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
	sort(process);	//도착시간 순으로 배열을 정렬

	while (1)
	{
		system("cls");
		// process의 도착시간이 현재시간 보다 큰지 확인
		if (process[currentProcess]->arrivalTime > t)
		{
			// 아직 도착하지 않은 상태이므로 해당 상태 출력
			work = 0;
			display(process, currentProcess, t, work);
		}
		else
		{
			// process가 도착한 경우 
			work = 1;

			// 모든 process의 잔여 시간이 0인지 확인
			check = 0;
			for (int i = 0; i < 5; i++)
			{
				check += process[i]->leftoverTime;
			}
			// 모든 process가 종료된 경우
			if (check <= 0)
			{
				work = -1;
				display(process, currentProcess, t, work);
				break;
			}

			// 현재 수행중인 process가 종료된 경우
			if (process[currentProcess]->leftoverTime == 0)
			{
				//수행중이던 process가 마지막 process면 종료
				if (currentProcess == 4)
				{
					work = -1;
					display(process, currentProcess, t, work);
					break;
				}
				currentProcess += 1;
				continue;
			}

			// 현재 상태 출력 및 현재 수행중인 process의 잔여시간 1 감소
			display(process, currentProcess, t, work);
			process[currentProcess]->leftoverTime -= 1;
		}

		// 현재 시간 1 증가
		t++;
		Sleep(2000);
	}

	// 모든 process가 종료되면 malloc으로 할당해준 memory 할당해제
	for (int i = 0; i < 5; i++)
	{
		free(process[i]);
	}

}


// 수행시간 제한 최대 100
void SJF(processStruct* process[]) {

	processStruct* temp;
	int t = 0;
	int work = 0;
	int currentProcess = 0;
	int min = 100;
	int check1;
	int check2 = 0;
	sort(process);	//도착시간 순으로 배열을 정렬


	while (1)
	{
		system("cls");
		// process의 도착시간이 현재시간 보다 큰지 확인
		if (process[currentProcess]->arrivalTime > t)
		{
			// 아직 도착하지 않은 상태이므로 해당 상태 출력
			work = 0;
			display(process, currentProcess, t, work);
		}
		else
		{
			// process가 도착한 경우 
			work = 1;

			if (process[currentProcess]->leftoverTime == 0)
			{
				// 현재 수행중이던 process가 수행이 완료되었을 경우

				// 수행시간이 가장 작은 process 찾기
				for (int i = 0; i < 5; i++)
				{
					// 현재 도착하지 않았거나 수행이 완료된 process는 제외
					if (process[i]->leftoverTime == 0 || process[i]->arrivalTime > t)
					{
						continue;
					}
					// 나머지 process 중 
					else if (process[i]->performTime < min)
					{
						// min보다 작은 값인 수행 시간을 가진 process를 현재 process로 변경
						min = process[i]->performTime;
						currentProcess = i;
					}
				}
				min = 100;

				// 위 과정을 커졌음에도 현재 process가 잔여 시간이 0인 경우, 아직 다음 proecess가 도착하지 않았거나 모든 process가 종료된 경우
				if (process[currentProcess]->leftoverTime == 0)
				{
					// 모든 process의 잔여시간을 확인하여 모든 process가 종료되었는지 확인
					check1 = 0;
					for (int i = 0; i < 5; i++)
					{
						check1 += process[i]->leftoverTime;
					}
					if (check1 == 0)
					{
						// 모든 process가 종료되었다면 프로그램 종료
						work = -1;
						display(process, currentProcess, t, work);
						break;
					}
					// 모든 process가 잔여시간이 0이거나 아직 도착한 process가 없는 경우
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
						// 현재 process가 없다는 상태를 출력하고 현재 시간을 1증가
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
			// 아직 잔여시간이 0이 아니고 process가 진행중인 경우 현재 상태 출력하고 잔여시간 1 감소
			display(process, currentProcess, t, work);
			process[currentProcess]->leftoverTime -= 1;
		}
		// 현재 시간 1증가
		t++;
		Sleep(2000);
	}

	// 모든 process가 종료되면 malloc으로 할당해준 메모리를 해제
	for (int i = 0; i < 5; i++)
	{
		free(process[i]);
	}

}


//선점
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
	sort(process);	//도착시간 순으로 배열을 정렬

	while (1)
	{
		system("cls");
		// process의 도착시간이 현재시간 보다 큰지 확인
		if (process[currentProcess]->arrivalTime > t)
		{
			// 아직 도착하지 않은 상태이므로 해당 상태 출력
			work = 0;
			display(process, currentProcess, t, work);
		}
		else
		{
			// process가 도착한 경우 
			work = 1;

			// 우선순위가 가장 높은 process 찾기
			for (int j = 0; j < 5; j++)
			{
				// 현재 도착하지 않았거나 수행이 완료된 process는 제외
				if (process[j]->leftoverTime == 0 || process[j]->arrivalTime > t)
				{
					continue;
				}
				// 나머지 process 중 
				else if (process[j]->priority <= max)
				{
					// 우선순위가 같으면 먼저들어온 process를 현재 process로 변경
					if (process[j]->priority == max)
					{
						currentProcess = max1;
					}
					// max보다 작은값인(우선순위가높은) 우선순위을 가진 process를 현재 process로 변경
					else
					{
						max = process[j]->priority;
						max1 = j;
						currentProcess = j;
					}
				}
				
			}
				max = 100;
			

				// 현재 process가 잔여 시간이 0인 경우에 아직 다음 proecess가 도착하지 않았거나모든 process가 종료된 경우
				if (process[currentProcess]->leftoverTime == 0)
				{
					// 모든 process의 잔여시간을 확인하여 모든 process가 종료되었는지 확인
					check1 = 0;
					for (int i = 0; i < 5; i++)
					{
						check1 += process[i]->leftoverTime;
					}
					if (check1 == 0)
					{
						// 모든 process가 종료되었다면 프로그램 종료
						work = -1;
						display(process, currentProcess, t, work);
						break;
					}
					// 모든 process가 잔여시간이 0이거나 아직 도착한 process가 없는 경우
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
						// 현재 process가 없다는 상태를 출력하고 현재 시간을 1증가
						system("cls");
						work = 0;
						check2 = 0;
						display(process, currentProcess, t, work);
						t++;
						Sleep(2000);
						continue;
					}
				}

				// 현재 상태 출력 및 현재 수행중인 process의 잔여시간 1 감소
				display(process, currentProcess, t, work);
				process[currentProcess]->leftoverTime -= 1;
		}

			// 현재 시간 1 증가
			t++;
			Sleep(2000);
	}

		// 모든 process가 종료되면 malloc으로 할당해준 memory 할당해제
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
	sort(process);	//도착시간 순으로 배열을 정렬

	while (1)
	{
		system("cls");
		// process의 도착시간이 현재시간 보다 큰지 확인
		if (process[currentProcess]->arrivalTime > t)
		{
			// 아직 도착하지 않은 상태이므로 해당 상태 출력
			work = 0;
			display(process, currentProcess, t, work);
		}
		else
		{
				// process가 도착한 경우 
				work = 1;
				// 수행시간이 가장 작은 process 찾기
				for (int k = 0; k < 5; k++)
				{
					// 현재 도착하지 않았거나 수행이 완료된 process는 제외
					if (process[k]->leftoverTime == 0 || process[k]->arrivalTime > t)
					{
						continue;
					}
					// 나머지 process 중 
					else if (process[k]->leftoverTime <= lot)
					{
						//lot와 잔여시간이 같은 process가 있으면 우선순위 높은 것부터 수행
						if (process[k]->leftoverTime == lot)
						{
							currentProcess = lot1;
						}
						// lot보다 작은 값인 잔여 시간을 가진 process를 현재 process로 변경
						else
						{
							lot = process[k]->leftoverTime;
							lot1 = k;
							currentProcess = k;
						}
					}
				}
				lot = 100;

				// 위 과정을 거쳤음에도 현재 process가 잔여 시간이 0인 경우, 아직 다음 proecess가 도착하지 않았거나 모든 process가 종료된 경우
				if (process[currentProcess]->leftoverTime == 0)
				{
					// 모든 process의 잔여시간을 확인하여 모든 process가 종료되었는지 확인
					check1 = 0;
					for (int i = 0; i < 5; i++)
					{
						check1 += process[i]->leftoverTime;
					}
					if (check1 == 0)
					{
						// 모든 process가 종료되었다면 프로그램 종료
						work = -1;
						display(process, currentProcess, t, work);
						break;
					}
					// 모든 process가 잔여시간이 0이거나 아직 도착한 process가 없는 경우
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
						// 현재 process가 없다는 상태를 출력하고 현재 시간을 1증가
						system("cls");
						work = 0;
						check2 = 0;
						display(process, currentProcess, t, work);
						t++;
						Sleep(2000);
						continue;
					}
				}
		
			// 아직 잔여시간이 0이 아니고 process가 진행중인 경우 현재 상태 출력하고 잔여시간 1 감소
			display(process, currentProcess, t, work);
			process[currentProcess]->leftoverTime -= 1;
		}
		// 현재 시간 1증가
		t++;
		Sleep(2000);
	}

		// 모든 process가 종료되면 malloc으로 할당해준 메모리를 해제
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
		// process의 도착시간이 현재시간 보다 큰지 확인
		if (process[currentProcess]->arrivalTime > t)
		{
			// 아직 도착하지 않은 상태이므로 해당 상태 출력
			work = 0;
			display(process, currentProcess, t, work);
		}
		else
		{
			// process가 도착한 경우 
			work = 1;
			
		
			// 모든 process의 잔여 시간이 0인지 확인
			check = 0;
			for (int i = 0; i < 5; i++)
			{
				check += process[i]->leftoverTime;
			}
			// 모든 process가 종료된 경우
			if (check <= 0)
			{
				work = -1;
				display(process, currentProcess, t, work);
				break;
			}
			
			// 현재 상태 출력 및 현재 수행중인 process의 잔여시간 1 감소, 2초마다 다음 process로 넘어감
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
			// 현재 수행중인 process가 종료되면 다음 process로 넘어가고 상태 출력
			else if (process[currentProcess]->leftoverTime == 0)
			{
				currentProcess += 1;
				display(process, currentProcess, t, work);
			}
		}
		// 현재 시간 1 증가
		t++;
		Sleep(2000);
	}

	// 모든 process가 종료되면 malloc으로 할당해준 memory 할당해제
	for (int i = 0; i < 5; i++)
	{
		free(process[i]);
	}
	
}


// 배열의 process들을 도착시간 순으로 정렬
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

// 현재 상태를 출력해주는 함수
void display(processStruct* process[], int num, int time, int work) {
	switch (work) {

	case 0:
		printf("시간: %d\b\n", time);
		printf("==================================================================================================================\n");
		printf("현재 수행중인 process가 없습니다.\b\n");
		printf("==================================================================================================================\n\n");
		for (int i = 0; i < 5; i++)
		{
			printf("Process : %s, Priority : %d, PerformTime : %d, ArrivalTime : %d, RemainingTime : %d \n", process[i]->name, process[i]->priority, process[i]->performTime, process[i]->arrivalTime, process[i]->leftoverTime);
		}
		break;


	case 1:
		printf("시간: %d\b\n", time);
		printf("==================================================================================================================\n");
		printf("현재 수행중인 process의 이름은: %s\b\n", process[num]->name);
		printf("==================================================================================================================\n\n");
		for (int i = 0; i < 5; i++)
		{
			printf("Process : %s, Priority : %d, PerformTime : %d, ArrivalTime : %d, RemainingTime : %d \n", process[i]->name, process[i]->priority, process[i]->performTime, process[i]->arrivalTime, process[i]->leftoverTime);
		}
		break;
	case -1:
		printf("시간: %d\b\n", time);
		printf("==================================================================================================================\n");
		printf("모든 process가 종료되었습니다. \b\n");
		printf("==================================================================================================================\n\n");
		break;
	}


}


// process를 생성해주는 함수
processStruct* createProcess(char* name, int priority, int performTime, int arrivalTime) {
	char* tempProcessName = (char*)malloc(sizeof(char) * MAX_NAME_LENGTH);
	processStruct* tempProcessStruct = (processStruct*)malloc(sizeof(processStruct));

	if (tempProcessName == NULL || tempProcessStruct == NULL)
	{
		perror("메모리 할당 오류");
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