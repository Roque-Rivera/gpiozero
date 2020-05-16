from gpiozero import LEDBarGraph
from time import sleep

graph = LEDBarGraph(10, 17, 27, 22, 18, 23)


while True:
    graph.value = 1  # (1, 1, 1, 1, 1, 1)
    sleep(1)
    graph.value = 1/2  # (1, 1, 1, 0, 0, 0)
    sleep(1)
    graph.value = -1/2  # (0, 0, 0, 1, 1, 1)
    sleep(1)
    graph.value = 1/4  # (1, 0, 0, 0, 0, 0)
    sleep(1)
    graph.value = -1  # (1, 1, 1, 1, 1, 1)
    sleep(1)
