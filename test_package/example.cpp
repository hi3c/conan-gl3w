#include <iostream>
#include <GL/gl3w.h>

int main() {
    if (gl3wInit())
        return 0;
    return 1;
}
