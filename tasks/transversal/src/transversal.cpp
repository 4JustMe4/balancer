#include <transversal.hpp>

#include <bitset>
#include <bit>
#include <cassert>
#include <chrono>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <sstream>

namespace {
    constexpr int MAX_SQUARE_SIZE = 64;

    inline auto getFormatedTime() {
        auto now = std::chrono::system_clock::now();
        std::time_t t = std::chrono::system_clock::to_time_t(now);
        std::tm tm = *std::localtime(&t);
        std::ostringstream oss;
        oss << std::put_time(&tm, "%H:%M:%S");
        return oss.str();
    }

    uint64_t transversalNumberImpl(
        const TSquare& s,
        int n,
        int row,
        uint64_t usedNumber,
        uint64_t allowedColumn
    ) {
        if (n == row) {
            return 1;
        }
        uint64_t ans = 0;
        for (uint64_t mask = allowedColumn; mask != 0; mask = mask & (mask - 1)) {
            uint32_t bit = mask & -mask;
            int i = std::countr_zero(bit); 
            if (!(usedNumber & (1 << s[row][i]))) {
                usedNumber ^= 1 << s[row][i];
                allowedColumn ^= 1 << i;
                ans += transversalNumberImpl(s, n, row + 1, usedNumber, allowedColumn);
                usedNumber ^= 1 << s[row][i];
                allowedColumn ^= 1 << i;
            }
        }
        return ans;
    }
}

uint64_t transversalNumber(const TSquare& s) {
    int limit = s.size() == 10 ? 40 : 1;
    uint64_t result;
    for (int i = 0; i < limit; i++) {
        std::cerr << getFormatedTime() << " Calc Transversal number" << std::endl;
        int n = s.size();
        uint64_t usedNumber = 0;
        uint64_t allowedColumn = (1 << n) - 1;
        assert(n < MAX_SQUARE_SIZE);
        result = transversalNumberImpl(s, n, 0, usedNumber, allowedColumn);
        std::cerr << getFormatedTime() << " End of calc" << std::endl;
    }
    return result;
}
