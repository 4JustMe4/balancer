#include <transversal.hpp>

#include <bitset>
#include <cassert>

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

    uint64_t transversalNumberImpl(
        const TSquare& s,
        int n,
        int row,
        std::bitset<MAX_SQUARE_SIZE>& usedNumber,
        std::bitset<MAX_SQUARE_SIZE>& usedCoulmn
    ) {
        if (n == row) {
            return 1;
        }
        uint64_t ans = 0;
        for (int i = 0; i < n; i++) {
            if (!usedNumber[s[row][i]] && !usedCoulmn[i]) {
                usedNumber[s[row][i]] = 1;
                usedCoulmn[i] = 1;
                ans += transversalNumberImpl(s, n, row + 1, usedNumber, usedCoulmn);
                usedNumber[s[row][i]] = 0;
                usedCoulmn[i] = 0;
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
        std::bitset<MAX_SQUARE_SIZE> usedNumber;
        std::bitset<MAX_SQUARE_SIZE> usedCoulmn;
        assert(n < MAX_SQUARE_SIZE);
        result = transversalNumberImpl(s, n, 0, usedNumber, usedCoulmn, 0, 0);
    }
    return result;
}
