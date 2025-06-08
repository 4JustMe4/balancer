#include <dtransversal.hpp>

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

    uint64_t dtransversalNumberImpl(
        const TSquare& s,
        int n,
        int row,
        uint64_t usedNumber,
        uint64_t allowedColumn,
        bool hasMain,
        bool hasSub
    ) {
        if (n == row) {
            if (hasMain && hasSub) {
                return 1;
            } else {
                return 0;
            }
        }
        uint64_t ans = 0;
        for (uint64_t mask = allowedColumn; mask != 0; mask = mask & (mask - 1)) {
            uint32_t bit = mask & -mask;
            int i = std::countr_zero(bit); 
            if (usedNumber & (1 << s[row][i]))
                continue;
            if (hasMain && i == row)
                continue;
            if (hasSub && i + row == n - 1)
                continue;

            allowedColumn ^= 1 << i;
            usedNumber ^= 1 << s[row][i];
            if (i == row) hasMain = true;
            if (i + row == n - 1) hasSub = true;
            ans += dtransversalNumberImpl(s, n, row + 1, usedNumber, allowedColumn, hasMain, hasSub);
            if (i == row) hasMain = false;
            if (i + row == n - 1) hasSub = false;
            allowedColumn ^= 1 << i;
            usedNumber ^= 1 << s[row][i];
        }
        return ans;
    }
}

uint64_t dtransversalNumber(const TSquare& s) {
    int limit = s.size() == 10 ? 40 : 1;
    uint64_t result;
    for (int i = 0; i < limit; i++) {
        std::cerr << getFormatedTime() << " Cacl DTransversal number" << std::endl;
        int n = s.size();
        uint64_t usedNumber = 0;
        uint64_t allowedColumn = (1 << n) - 1;
        assert(n < MAX_SQUARE_SIZE);
        result = dtransversalNumberImpl(s, n, 0, usedNumber, allowedColumn, 0, 0);
        std::cerr << getFormatedTime() << " End of calc" << std::endl;
    }
    return result;
}
