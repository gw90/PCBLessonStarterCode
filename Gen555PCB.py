from Gen555Components import *

# Top-Level
class Gen555PCB(SimpleBoardTop):
    def contents(self) -> None:
        super().contents()

if __name__ == "__main__":
    compile_board_inplace(Gen555PCB)
