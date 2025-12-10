Test Plan – Solar System Program

The purpose of this test plan is to check that the Solar System program works properly and responds correctly to different types of user input. The program should show information about planets, handle mistakes without crashing, and let the user exit safely.

The program is tested using Python 3 and Visual Studio Code, running it in the terminal. All planet data is stored directly inside the code.

First, I will check that the program starts correctly. When running python main.py, the program should display the introduction and wait for a question.

Next, I will test the feature that shows full information about a planet. For example, if I type “tell me everything about earth”, the program should print Earth’s name, mass, distance from the Sun and its moon. I will also test this with Saturn to make sure it works for more than one planet.

Then I will test questions about the number of moons. If I type “how many moons does mars have”, the program should reply that Mars has 2 moons. If I ask the same question for Mercury, it should say that Mercury has 0 moons.

After that, I will test the questions about a planet’s mass. For example, “how massive is jupiter” should display Jupiter’s mass, and “how massive is neptune” should show Neptune’s mass.

I will then test whether the program correctly identifies if a planet is included in the list. If I type “is earth in the list of planets”, the program should say yes. If I type “is pluto in the list of planets”, it should say no, because Pluto has been removed.

I will also check input validation. If I press enter without typing anything, the program should ask me to type a question. If I type something that makes no sense, like “banana spaceship”, the program should respond with “Invalid Question.”

Finally, I will test that the program can exit properly. Typing “quit” should close the program without errors.

This test plan covers the main features of the Solar System program and confirms that the program behaves correctly for valid input, invalid input and edge cases.
