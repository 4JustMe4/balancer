#include <transversal.hpp>

#include <bitset>
#include <cassert>
#include <chrono>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <sstream>

namespace {
    constexpr int MAX_SQUARE_SIZE = 32;

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
        uint32_t usedNumber,
        uint32_t usedCoulmn
    ) {
        if (n == row) {
            return 1;
        }
        uint64_t ans = 0;
        for (int i = 0; i < n; i++) {
            if (!(usedCoulmn & (1 << i)) && !(usedNumber & (1 << s[row][i]))) {
                usedNumber ^= 1 << s[row][i];
                usedCoulmn ^= 1 << i;
                ans += transversalNumberImpl(s, n, row + 1, usedNumber, usedCoulmn);
                usedNumber ^= 1 << s[row][i];
                usedCoulmn ^= 1 << i;
            }
        }
        return ans;
    }
}

uint64_t transversalNumber(const TSquare& s) {
    int limit = s.size() == 10 ? 40 : 1;
    uint64_t result;
    for (int i = 0; i < limit; i++) {
        std::cerr << getFormatedTime() << " Cacl Transversal number" << std::endl;
        int n = s.size();
        uint64_t usedNumber = 0;
        uint64_t usedCoulmn = 0;
        assert(n < MAX_SQUARE_SIZE);
        result = transversalNumberImpl(s, n, 0, usedNumber, usedCoulmn);
    }
    return result;
}
