class MyQueue:

    def __init__(self,value):
        self.input = [] # 입구
        self.output = [] # 출구

    def push(self, x: int) -> None:
        self.input.append(x) # (오른쪽입구기준) 전달받은 값을 입구에 넣어준다

    def pop(self) -> int:
        self.peek() # 입구로 들어온 순서를 뒤집어 준다
        return self.output.pop() # 순서가 뒤집혔기 때문에 제일 먼저 입구에 들어온 값이 마지막 값이되어 삭제

    def peek(self) -> int:
        if not self.output: # 출구로 나가는 값이 없으면 실행
            while self.input: # 입구로 들어온 값이 없을때 까지 실행
                self.output.append(self.input.pop()) # 마지막으로 입구로 들어온 값부터 출구로 보내줌
        return self.output[-1] # 제일 먼저 출구로 갈 값이 제일 먼저 들어온 값이기 때문에 먼저 출구로 갈 값을 반환

    def empty(self) -> bool: # 큐가 비어 있는지 확인
        return self.input == [] and self.output == []