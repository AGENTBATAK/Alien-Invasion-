#include <windows.h>

extern "C" {

    __declspec(dllexport) bool moveUp() {
        return GetAsyncKeyState('W') & 0x8000;
    }

    __declspec(dllexport) bool moveDown() {
        return GetAsyncKeyState('S') & 0x8000;
    }

    __declspec(dllexport) bool moveLeft() {
        return GetAsyncKeyState('A') & 0x8000;
    }

    __declspec(dllexport) bool moveRight() {
        return GetAsyncKeyState('D') & 0x8000;
    }
    __declspec(dllexport) bool spacedown() {
        return GetAsyncKeyState(VK_SPACE) & 0x8000;
    }
}
