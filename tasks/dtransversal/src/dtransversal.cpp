#include <dtransversal.hpp>

#include <bitset>
#include <cassert>
#include <chrono>
#include <ctime>
#include <iomanip>
#include <iostream>

namespace {
    constexpr int MAX_SQUARE_SIZE = 128;

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
        std::bitset<MAX_SQUARE_SIZE>& usedNumber,
        std::bitset<MAX_SQUARE_SIZE>& usedCoulmn,
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
        for (int i = 0; i < n; i++) {
            if (hasMain && i == row)
                continue;
            if (hasSub && i + row == n - 1)
                continue;
            if (usedNumber[s[row][i]])
                continue;
            if (usedCoulmn[i])
                continue;

            usedCoulmn[i] = usedNumber[s[row][i]] = 1;
            if (i == row) hasMain = true;
            if (i + row == n - 1) hasSub = true;
            ans += dtransversalNumberImpl(s, n, row + 1, usedNumber, usedCoulmn, hasMain, hasSub);
            if (i == row) hasMain = false;
            if (i + row == n - 1) hasSub = false;
            usedCoulmn[i] = usedNumber[s[row][i]] = 0;
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
        std::bitset<MAX_SQUARE_SIZE> usedNumber;
        std::bitset<MAX_SQUARE_SIZE> usedCoulmn;
        assert(n < MAX_SQUARE_SIZE);
        result = dtransversalNumberImpl(s, n, 0, usedNumber, usedCoulmn, 0, 0);
    }
    return result;
}
