CXX = g++

FLAGS = -std=c++17 -O0 --coverage
LIBS = -lgtest -lgtest_main -pthread

SRC = main.cpp stack.cpp queue.cpp tree.cpp test.cpp

TARGET = tests
REPORT = coverage_report

all:
	$(CXX) $(FLAGS) $(SRC) $(LIBS) -o $(TARGET)

run: all
	./$(TARGET)

coverage:
	rm -f *.gcda *.gcno coverage.info
	$(CXX) $(FLAGS) $(SRC) $(LIBS) -o $(TARGET)
	./$(TARGET)

	lcov --capture --directory . \
	--output-file coverage.info \
	--ignore-errors inconsistent,unexecuted

	lcov --remove coverage.info '/usr/*' '*/test.cpp' \
	--output-file coverage.info

	genhtml coverage.info --output-directory $(REPORT)

	@echo "Open $(REPORT)/index.html"

clean:
	rm -f $(TARGET) *.gcda *.gcno coverage.info
	rm -rf $(REPORT)