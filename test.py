from manimlib import *
class Test(Scene):
    def construct(self):
        words=Text("""
            let's start to make
            dumplings  
        """)
        words.to_edge(UP)
        self.play(Write(words))
        self.wait(2)

        grid = NumberPlane((-10, 10), (-5, 5))
        matrix = [[1, 1], [0, 2]]
        linear_transform_words = VGroup(
            Text("This is what the matrix"),
            IntegerMatrix(matrix, include_background_rectangle=True),
            Text("looks like")
        )
        linear_transform_words.arrange(RIGHT)
        linear_transform_words.to_edge(UP)
        linear_transform_words.set_backstroke(width=5)
        self.play(
            ShowCreation(grid),
            FadeTransform(words, linear_transform_words)
        )
        self.wait()
        self.play(grid.animate.apply_matrix(matrix), run_time=3)
        self.wait()
