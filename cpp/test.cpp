#include <gtest/gtest.h>
#include "stack.h"

TEST(StackTest, PushPop) {
    Stack s;
    s.push(5);
    EXPECT_EQ(s.peek(), 5);

    s.pop();
    EXPECT_EQ(s.peek(), -1);
}